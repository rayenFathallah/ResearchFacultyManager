<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Publications</h1>
          <hr/>
          <br/><br/>
          <alert v-if="showMessage" :message="message"></alert>
          <button
              class="btn btn-success btn-sm"
              type="button"
              @click="toggleAddPublicationModal">
            Ajouter une publication
          </button>
          <br/><br/>
          <div class="labo_filter">Filtrer par chercheur : 
          <select class="form-select selectForm__inner" data-trigger="true" name="choices-single-location" id="choices-single-location" aria-label="Default select example" v-model="this.selected_chercheur">
            <option v-for=" ch in this.chercheurs" :key="ch.chnom" v-bind:value="ch.chnom">{{ ch.chnom }}</option>
          </select>
        </div>
          <div class="col-lg-3 adjust_margin">
          <div>
            <a class="btn btn-primary " @click="filter_publications"><i class="uil uil-filter"></i> Filter</a><a class="btn btn-primary " @click="reset_publications"><i class="uil uil-filter"></i> Reset</a>
          </div>
        </div>
          <table class="table table-hover">
            <thead>
            <tr>
              <th scope="col">Titre du publication</th>
              <th scope="col">Theme</th>
              <th scope="col">Type</th>
              <th scope="col">Volume</th>
              <th scope="col">Date</th>
              <th scope="col">Apparition</th>
              <th scope = "col">Editeur</th>
              <th scope = "cpm">Date de publication</th>

            </tr>
            </thead>
            <tbody>
            <tr v-for="(Publication, index) in filtered_publications" :key="index">
              <td>{{ Publication.titre }}</td>
              <td>{{ Publication.theme }}</td>
              <td>{{ Publication.type }}</td>
              <td>{{ Publication.volume }}</td>
              <td>{{ Publication.date }}</td>
              <td>{{ Publication.apparition }}</td>
              <td>{{ Publication.editeur }}</td>
              <td>{{ Publication.pubno }}</td>

              <td>
                <div class="btn-group" role="group">
                  <button
                      class="btn btn-warning btn-sm"
                      type="button"
                      @click="toggleEditPublicationModal(Publication)">
                    Update
                  </button>
                  <button
                      class="btn btn-danger btn-sm"
                      type="button"
                      @click="handleDeletePublication(Publication)">
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
    <!-- add new Publication modal -->
    <div
        ref="addPublicationModal"
        :class="{ show: activeAddPublicationModal, 'd-block': activeAddPublicationModal }"
        class="modal fade"
        role="dialog"
        tabindex="-1">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new Publication</h5>
            <button
                aria-label="Close"
                class="close"
                data-dismiss="modal"
                type="button"
                @click="toggleAddPublicationModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
                <div class="mb-3">
                <label class="form-label" for="addPublicationdate_pub">Identificateur:</label>
                <input
                    id="addPublicationdate_pub"
                    v-model="addPublicationForm.pubno"
                    class="form-control"
                    placeholder="AA-NNNN format"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationname">Titre du Publication:</label>
                <input
                    id="addPublicationName"
                    v-model="addPublicationForm.titre"
                    class="form-control"
                    placeholder="Entrez le nom du Publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationtheme">Theme du Publication:</label>
                <input
                    id="addPublicationtheme"
                    v-model="addPublicationForm.theme"
                    class="form-control"
                    placeholder="Entrez le theme du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationtype">Type de Publication:</label>
                <input
                    id="addPublicationtype"
                    v-model="addPublicationForm.type"
                    class="form-control"
                    placeholder="Entrez le type du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationvolume">Volume du Publication:</label>
                <input
                    id="addPublicationvolume"
                    v-model="addPublicationForm.volume"
                    class="form-control"
                    placeholder="Entrez le volume du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationEditor">Editeur du Publication:</label>
                <input
                    id="addPublicationEditor"
                    v-model="addPublicationForm.editeur"
                    class="form-control"
                    placeholder="Entrez l'editeur du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationdate">Date de la parution de la publication:</label>
                <input
                    id="addPublicationdate"
                    v-model="addPublicationForm.date"
                    class="form-control"
                    placeholder="Entrez la date de parution"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addPublicationapparition">Apparition du Publication:</label>
                <input
                    id="addPublicationapparition"
                    v-model="addPublicationForm.apparition"
                    class="form-control"
                    placeholder="Entrez l'apparition du publication"
                    type="text"/>
              </div>
              <div class= "mb-3"> 
                <label class="form-label" for="addPublicationauthors">Les auteurs de la publication:</label>
                <select id = "addPublicationauthors" multiple v-model = "addPublicationForm.chercheurs">
                  <option v-for="(option, index) in chercheurs" :key="option.chno" :value="option.chno">
                    {{ option.chnom }}
                  </option>
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
    <div v-if="activeAddPublicationModal" class="modal-backdrop fade show"></div>
    <!-- edit Publication modal -->
    <div
        ref="editPublicationModal"
        :class="{ show: activeEditPublicationModal, 'd-block': activeEditPublicationModal }"
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
                @click="toggleEditPublicationModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label class="form-label" for="editPublicationName">Nom du Publication:</label>
                <input
                    id="editPublicationName"
                    v-model="editPublicationForm.titre"
                    class="form-control"
                    placeholder="Enter the new Publication name"
                    type="text">
              </div>
              <div class="mb-3">
                <label class="form-label" for="editPublicationtheme">Theme du Publication:</label>
                <input
                    id="editPublicationtheme"
                    v-model="editPublicationForm.theme"
                    class="form-control"
                    placeholder="Entrez le theme du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="editPublicationtype">Type de Publication:</label>
                <input
                    id="editPublicationtype"
                    v-model="editPublicationForm.type"
                    class="form-control"
                    placeholder="Entrez le type du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="editPublicationvolume">Volume du Publication:</label>
                <input
                    id="editPublicationvolume"
                    v-model="editPublicationForm.volume"
                    class="form-control"
                    placeholder="Entrez le volume du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="editPublicationEditor">Editeur du Publication:</label>
                <input
                    id="editPublicationEditor"
                    v-model="editPublicationForm.editeur"
                    class="form-control"
                    placeholder="Entrez l'editeur du publication"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="editPublicationdate">Date de la parution de la publication:</label>
                <input
                    id="editPublicationdate"
                    v-model="editPublicationForm.date"
                    class="form-control"
                    placeholder="Entrez la date de parution"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="editPublicationapparition">Apparition du Publication:</label>
                <input
                    id="editPublicationapparition"
                    v-model="editPublicationForm.apparition"
                    class="form-control"
                    placeholder="Entrez l'apparition du publication"
                    type="text"/>
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
    <div v-if="activeEditPublicationModal" class="modal-backdrop fade show"></div>
  </template>
  
  <script>
  import axios from "axios";
  import Alert from "./Alert.vue";
  
  export default {
    data() {
      return {
        activeAddPublicationModal: false,
        filtered_publications:[],
        selected_chercheur : "",
        addPublicationForm: {
          titre: '',
          theme : '', 
          type :'' ,
          volume : '',
          date : '',
          apparition : '' ,
          editeur : '',
          chercheurs : []
        },
        chercheurs :[],
        activeEditPublicationModal: false,
        editPublicationForm: {
          titre: '',
          theme : '', 
          type :'' ,
          volume : '',
          date : '',
          apparition : '' ,
          editeur : '' 
        },
        publications: [],
        message: "",
        showMessage: false,
      };
    },
    components: {
      alert: Alert,
    },
    methods: {
      addPublication(payload) {
        const path = "http://localhost:5001/publications";
        axios
            .post(path, payload)
            .then(response => {
                // Assuming your Flask server sends the message in the response
                this.message = response.data.message;
                console.log('here is you payload'); 
                console.log(payload);
                this.getpublications();
                this.showMessage = true;
            })
            .catch((error) => {
              console.log(error);
              this.getpublications();
            });
      },
      getpublications() {
        const path = "http://localhost:5001/publicas";
        axios
            .get(path)
            .then((res) => {
              this.publications = res.data.items.publicas;
              this.filtered_publications = res.data.items.publicas;
              console.log("these are you publications");
              console.log(this.publications);
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
      handleAddReset() {
        this.initForm();
      },
      handleAddSubmit() {
        this.toggleAddPublicationModal();
 
        const payload = {
          titre: this.addPublicationForm.titre,
          theme : this.addPublicationForm.theme, 
          type :this.addPublicationForm.type ,
          volume : this.addPublicationForm.volume,
          date : this.addPublicationForm.date,
          apparition : this.addPublicationForm.apparition ,
          editeur : this.addPublicationForm.editeur,
          pubno : this.addPublicationForm.pubno,
          chercheurs : this.addPublicationForm.chercheurs

        };
        this.addPublication(payload);
        this.initForm();
      },
      initForm() {
        this.addPublicationForm.titre = "",
        this.addPublicationForm.theme = "", 
        this.addPublicationForm.type="" ,
        this.addPublicationForm.volume="",
        this.addPublicationForm.date="",
        this.addPublicationForm.apparition="" ,
        this.addPublicationForm.editeur=""
        this.addPublicationForm.pubno = ""
      },
      toggleAddPublicationModal() {
        const body = document.querySelector("body");
        this.activeAddPublicationModal = !this.activeAddPublicationModal;
        if (this.activeAddPublicationModal) {
          body.classList.add("modal-open");
        } else {
          body.classList.remove("modal-open");
        }
      },
      toggleEditPublicationModal(Publication) {
        if (Publication) {
          this.editPublicationForm = Publication;
        }
        const body = document.querySelector("body");
        this.activeEditPublicationModal = !this.activeEditPublicationModal;
        if (this.activeEditPublicationModal) {
          body.classList.add("modal-open");
        } else {
          body.classList.remove("modal-open");
        }
      },
      handleEditSubmit() {
        this.toggleEditPublicationModal(null);
        let read = false;
        if (this.editPublicationForm.read) read = true;
        const payload = {
            titre: this.editPublicationForm.titre,
            theme : this.editPublicationForm.theme, 
            type :this.editPublicationForm.type ,
            volume : this.editPublicationForm.volume,
            date : this.editPublicationForm.date,
            apparition : this.editPublicationForm.apparition ,
            editeur : this.editPublicationForm.editeur
        };
        this.updatePublication(payload, this.editPublicationForm.labno);
      },
      updatePublication(payload, LabID) {
        const path = `http://localhost:5001/publications/${LabID}`;
        axios.put(path, payload)
            .then(() => {
              this.getpublications();
              this.message = 'Publication updated!';
              this.showMessage = true;
            })
            .catch((error) => {
              console.error(error);
              this.getpublications();
            });
      },
      handleEditCancel() {
        this.toggleEditPublicationModal(null);
        this.initForm();
        this.getpublications(); // why?
      },
      handleDeletePublication(Publication) {
        this.removePublication(Publication.pubno);
      },
      removePublication(PublicationID) {
        const path = `http://localhost:5001/publications/${PublicationID}`;
        axios.delete(path)
            .then(() => {
              this.getpublications();
              this.message = 'Publication removed!';
              this.showMessage = true;
            })
            .catch((error) => {
              console.error(error);
              this.getpublications();
            });
      },
      filter_publications() {
      this.filtered_publications = this.filterPublications;
      },
      filterPub_meth(pubs) {
        return pubs.filter(ch => {
            if (this.selected_chercheur) {
                return ch.chercheurs.includes(this.selected_chercheur);
            } else {
                return true;
            }
            });
      },
      reset_publications() {
        this.filtered_publications = this.publications;
      }
    },
    computed : {
    filterPublications() {
    let filtered_publications = this.publications; 
    return this.filterPub_meth(filtered_publications)
    }

  },
    created() {
      this.getpublications();
      this.getchercheurs();
    },
  };
  </script>
  