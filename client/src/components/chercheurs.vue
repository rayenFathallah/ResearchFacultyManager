<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Chercheurs</h1>
        <hr/>
        <br/><br/>
        <alert v-if="showMessage" :message="message"></alert>
        <button
            class="btn btn-success btn-sm"
            type="button"
            @click="toggleAddChercheurModal">
          Ajouter un chercheur
        </button>
        <br/><br/>
        <div class="labo_filter">
          Filtrer par laboratoire : 
          <select class="form-select selectForm__inner" data-trigger="true" name="choices-single-location" id="choices-single-location" aria-label="Default select example" v-model="this.selected_labo">
            <option v-for=" lab in this.labos" :key="lab.labno" v-bind:value="lab.labno">{{ lab.labnom }}</option>
          </select>
        </div>
        <div class="col-lg-3 adjust_margin">
          <div>
            <a class="btn btn-primary " @click="filter_chercheurs"><i class="uil uil-filter"></i> Filter</a><a class="btn btn-primary " @click="reset_labos"><i class="uil uil-filter"></i> Reset</a>
          </div>
        </div>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Nom du chercheur</th>
            <th scope="col">Grade</th>
            <th scope="col">Statut</th>
            <th scope="col">Daterecrut</th>
            <th scope="col">Salaire</th>
            <th scope="col">Prime</th>
            <th scope="col">Email</th>
            <th scope="col">Superieur</th>
            <th scope="col">laboratoire</th>
            <th scope="col">Faculté</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(Chercheur, index) in filtered_chercheurs" :key="index">
            <td>{{ Chercheur.chnom }}</td>
            <td>{{ Chercheur.grade }}</td>
            <td>{{ Chercheur.statut }}</td>
            <td>{{ Chercheur.datarecrut }}</td>
            <td>{{ Chercheur.salaire }}</td>
            <td>{{ Chercheur.prime }}</td>
            <td>{{ Chercheur.email }}</td>
            <td v-if = Chercheur.supno>{{ get_superieur(Chercheur.supno) }}</td>
            <td v-else>Pas de superviseur</td>
            <td>{{ get_labo(Chercheur.labno) }}</td>
            <td>{{ get_faculty(Chercheur.facno) }}</td>
            <td>
              <div class="btn-group" role="group">
                <button
                    class="btn btn-warning btn-sm"
                    type="button"
                    @click="toggleEditChercheurModal(Chercheur)">
                  Update
                </button>
                <button
                    class="btn btn-danger btn-sm"
                    type="button"
                    @click="handleDeleteChercheur(Chercheur)">
                  Delete
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <!-- add new Chercheur modal -->
  <div
      ref="addChercheurModal"
      :class="{ show: activeAddChercheurModal, 'd-block': activeAddChercheurModal }"
      class="modal fade"
      role="dialog"
      tabindex="-1">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Ajouter un nouveau chercheur</h5>
          <button
              aria-label="Close"
              class="close"
              data-dismiss="modal"
              type="button"
              @click="toggleAddChercheurModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label" for="addChercheurname">Nom du Chercheur:</label>
              <input
                  id="addChercheurName"
                  v-model="addChercheurForm.chnom"
                  class="form-control"
                  placeholder="Entrez le nom du Chercheur"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addChercheurgrade">Grade:</label>
              <input
                  id="addChercheurGrade"
                  v-model="addChercheurForm.grade"
                  class="form-control"
                  placeholder="E , D , A , MA, MC , PR"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addChercheurstatut">Statut:</label>
              <input
                  id="addChercheurStatut"
                  v-model="addChercheurForm.statut"
                  class="form-control"
                  placeholder="P , C"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addChercheurdate">Date de recrutement:</label>
              <input
                  id="addChercheurDate"
                  v-model="addChercheurForm.daterecrut"
                  class="form-control"
                  placeholder="Entrez la Date de recrutement du Chercheur"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addChercheursalaire">Salaire:</label>
              <input
                  id="addChercheursalaire"
                  v-model="addChercheurForm.salaire"
                  class="form-control"
                  placeholder="Entrez le salaire du Chercheur"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addChercheurprime">Prime:</label>
              <input
                  id="addChercheurprime"
                  v-model="addChercheurForm.prime"
                  class="form-control"
                  placeholder="Entrez le salaire du Prime"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addChercheuremail">Email:</label>
              <input
                  id="addChercheursEmail"
                  v-model="addChercheurForm.email"
                  class="form-control"
                  placeholder="Entrez l'email du Chercheur"
                  type="text"/>
            </div>
          
            <div class="mb-3">
              <label for="facultySelect">Select a Faculty:</label>
              <select v-model="addChercheurForm.facno" id="facultySelect">
                  <option v-for="faculty in this.faculties" :key="faculty.facno" :value="faculty.facno">{{ faculty.facnom }}</option>
              </select>
            </div>
            <div class="mb-3">
              <label for="labSelect">Selectionnez un laboratoire:</label>
              <select v-model="addChercheurForm.labno" id="labSelect">
                  <option v-for="lab in this.labos" :key="lab.labno" :value="lab.labno">{{ lab.labnom }}</option>
              </select>
            </div>
            <div class="mb-3">
              <label for="superiorSelect">Selectionnez le superieur:</label>
              <select v-model="addChercheurForm.supno" id="superiorSelect">
                  <option v-for="superior in this.chercheurs" :key="superior.chno" :value="superior.chno">{{ superior.chnom }}</option>
              </select>
            </div>

            <div class="btn-group" role="group">
              <button
                  class="btn btn-primary btn-sm"
                  type="button"
                  @click="handleAddSubmit">
                Submit
              </button>
              <button
                  class="btn btn-danger btn-sm"
                  type="button"
                  @click="handleAddReset">
                Reset
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="activeAddChercheurModal" class="modal-backdrop fade show"></div>
  <!-- edit Chercheur modal -->
  <div
      ref="editChercheurModal"
      :class="{ show: activeEditChercheurModal, 'd-block': activeEditChercheurModal }"
      class="modal fade"
      role="dialog"
      tabindex="-1">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Update</h5>
          <button
              aria-label="Close"
              class="close"
              data-dismiss="modal"
              type="button"
              @click="toggleEditChercheurModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label" for="editChercheurName">Nom du Chercheur:</label>
              <input
                  id="editChercheurName"
                  v-model="editChercheurForm.labnom"
                  class="form-control"
                  placeholder="Enter the new Chercheur name"
                  type="text">
            </div>
            <div class="mb-3">
              <label for="facultySelect">Select a Faculty:</label>
              <select v-model="editChercheurForm.facno" id="facultySelect">
                  <option v-for="faculty in this.faculties" :key="faculty.facno" :value="faculty.facno">{{ faculty.facnom }}</option>
              </select>
            </div>
            <div class="btn-group" role="group">
              <button
                  class="btn btn-primary btn-sm"
                  type="button"
                  @click="handleEditSubmit">
                Submit
              </button>
              <button
                  class="btn btn-danger btn-sm"
                  type="button"
                  @click="handleEditCancel">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="activeEditChercheurModal" class="modal-backdrop fade show"></div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert.vue";

export default {
  data() {
    return {
      activeAddChercheurModal: false,
      addChercheurForm: {
        chnom: "",
        grade : "", 
        statut: "", 
        daterecrut : "",
        salaire : null,
        prime: null,
        email : "", 
        supno : null,
        labno : null,
        facno: null,
      },
      selected_labo : null,
      activeEditChercheurModal: false,
      editChercheurForm: {
        chnom: "",
        grade : "", 
        statut: "", 
        daterecrut : "",
        salaire : null,
        prime: null,
        email : "", 
        supno : null,
        labno : null,
        facno: null,
      },
      chercheurs: [],
      filtered_chercheurs : [],
      faculties : [],
      labos : [],
      message: "",
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    addChercheur(payload) {
      const path = "http://localhost:5001/chercheurs";
      axios
          .post(path, payload)
          .then(response => {
              // Assuming your Flask server sends the message in the response
              this.message = response.data.message;
              console.log("this is the payload"); 
              console.log(payload);
              this.getchercheurs();
              this.showMessage = true;
          })
          .catch((error) => {
            console.log(error);
            console.log(payload);
            this.getchercheurs();
          });
    },
    get_faculty(id) {
      for(let elem of this.faculties) {
          if (elem.facno == id) {
              return elem.facnom;
          }
      }
    },
    get_labo(id) {
      for(let elem of this.labos) {
          if (elem.labno == id) {
              return elem.labnom;
          }
      }
    },
    get_superieur(id) {
      for(let elem of this.chercheurs) {
          if (elem.chno == id) {
              return elem.chnom;
          }
      }
    },
    getfaculties() {
      const path = "http://localhost:5001/faculties";
      axios
          .get(path)
          .then((res) => {
            this.faculties = res.data.items.faculties;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    getchercheurs() {
      const path = "http://localhost:5001/chercheurs";
      axios
          .get(path)
          .then((res) => {
            this.chercheurs = res.data.items.chercheurs;
            this.filtered_chercheurs = res.data.items.chercheurs;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    getlabos() {
        const path = "http://localhost:5001/labos";
        axios
            .get(path)
            .then((res) => {
              this.labos = res.data.items.labos;
            })
            .catch((error) => {
              console.error(error);
            });
      },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddChercheurModal();

      const payload = {
        chnom: this.addChercheurForm.chnom,
        grade : this.addChercheurForm.grade,
        statut: this.addChercheurForm.statut, 
        daterecrut : this.addChercheurForm.daterecrut,
        salaire : this.addChercheurForm.salaire,
        prime: this.addChercheurForm.prime,
        email : this.addChercheurForm.email, 
        supno : this.addChercheurForm.supno,
        labno : this.addChercheurForm.labno,
        facno: this.addChercheurForm.facno,
      };
      this.addChercheur(payload);
      this.initForm();
    },
    initForm() {
        this.addChercheurForm.chnom = "",
        this.addChercheurForm.grade= "",
        this.addChercheurForm.statut="", 
        this.addChercheurForm.daterecrut="",
        this.addChercheurForm.salaire= null,
        this.addChercheurForm.prime = null,
        this.addChercheurForm.email="", 
        this.addChercheurForm.supno = null,
        this.addChercheurForm.labno = null,
        this.addChercheurForm.facno= null
    },
    toggleAddChercheurModal() {
      const body = document.querySelector("body");
      this.activeAddChercheurModal = !this.activeAddChercheurModal;
      if (this.activeAddChercheurModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
    toggleEditChercheurModal(Chercheur) {
      if (Chercheur) {
        this.editChercheurForm = Chercheur;
      }
      const body = document.querySelector("body");
      this.activeEditChercheurModal = !this.activeEditChercheurModal;
      if (this.activeEditChercheurModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
    handleEditSubmit() {
      this.toggleEditChercheurModal(null);
      let read = false;
      if (this.editChercheurForm.read) read = true;
      const payload = {
        facno: this.editChercheurForm.facno,
        labnom: this.editChercheurForm.labnom,
      };
      this.updateChercheur(payload, this.editChercheurForm.labno);
    },
    updateChercheur(payload, LabID) {
      const path = `http://localhost:5001/chercheurs/${LabID}`;
      axios.put(path, payload)
          .then(() => {
            this.getchercheurs();
            this.message = 'Chercheur updated!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getchercheurs();
          });
    },
    handleEditCancel() {
      this.toggleEditChercheurModal(null);
      this.initForm();
      this.getchercheurs(); // why?
    },
    handleDeleteChercheur(Chercheur) {
      this.removeChercheur(Chercheur.chno);
    },
    removeChercheur(ChercheurID) {
      const path = `http://localhost:5001/chercheurs/${ChercheurID}`;
      axios.delete(path)
          .then(() => {
            this.getchercheurs();
            this.message = 'Chercheur removed!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getchercheurs();
          });
    },
    filter_chercheurs() {
      this.filtered_chercheurs = this.filterCherch;
      console.log('here are your filtered elements'); 
      console.log(this.filtered_chercheurs); 

    },
    filtercherch_meth(cherchs) {
            return cherchs.filter(ch => {
            if (this.selected_labo) {
                return ch.labno == this.selected_labo;
            } else {
                return true;
            }
            });
    },
    reset_labos(){
      this.filtered_chercheurs = this.chercheurs;
    }
  },
  computed : {
    filterCherch() {
    let filtered_researcher = this.chercheurs; 
    return this.filtercherch_meth(filtered_researcher)
    }

  },
  created() {
    this.getchercheurs();
    this.getfaculties();
    this.getlabos();
  }
};
</script>
