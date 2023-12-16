<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Laboratoires</h1>
          <hr/>
          <br/><br/>
          <alert v-if="showMessage" :message="message"></alert>
          <button
              class="btn btn-success btn-sm"
              type="button"
              @click="toggleAddLaboModal">
            Ajouter un laboratoire
          </button>
          <br/><br/>
          <table class="table table-hover">
            <thead>
            <tr>
              <th scope="col">Nom de laboratoire</th>
              <th scope="col">Faculté</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(Labo, index) in labos" :key="index">
              <td>{{ Labo.labnom }}</td>
              <td> {{ get_faculty(Labo.facno) }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                      class="btn btn-warning btn-sm"
                      type="button"
                      @click="toggleEditLaboModal(Labo)">
                    Update
                  </button>
                  <button
                      class="btn btn-danger btn-sm"
                      type="button"
                      @click="handleDeleteLabo(Labo)">
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
    <!-- add new Labo modal -->
    <div
        ref="addLaboModal"
        :class="{ show: activeAddLaboModal, 'd-block': activeAddLaboModal }"
        class="modal fade"
        role="dialog"
        tabindex="-1">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new Labo</h5>
            <button
                aria-label="Close"
                class="close"
                data-dismiss="modal"
                type="button"
                @click="toggleAddLaboModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label class="form-label" for="addLaboname">Nom du laboratoire:</label>
                <input
                    id="addLaboName"
                    v-model="addLaboForm.labnom"
                    class="form-control"
                    placeholder="Entrez le nom du laboratoire"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label for="facultySelect">Select a Faculty:</label>
                <select v-model="addLaboForm.facno" id="facultySelect">
                    <option v-for="faculty in this.faculties" :key="faculty.facno" :value="faculty.facno">{{ faculty.facnom }}</option>
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
    <div v-if="activeAddLaboModal" class="modal-backdrop fade show"></div>
    <!-- edit Labo modal -->
    <div
        ref="editLaboModal"
        :class="{ show: activeEditLaboModal, 'd-block': activeEditLaboModal }"
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
                @click="toggleEditLaboModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label class="form-label" for="editLaboName">Nom du labo:</label>
                <input
                    id="editLaboName"
                    v-model="editLaboForm.labnom"
                    class="form-control"
                    placeholder="Enter the new Labo name"
                    type="text">
              </div>
              <div class="mb-3">
                <label for="facultySelect">Select a Faculty:</label>
                <select v-model="editLaboForm.facno" id="facultySelect">
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
    <div v-if="activeEditLaboModal" class="modal-backdrop fade show"></div>
  </template>
  
  <script>
  import axios from "axios";
  import Alert from "./Alert.vue";
  
  export default {
    data() {
      return {
        activeAddLaboModal: false,
        addLaboForm: {
          labnom: "",
          facno: null,
        },
        activeEditLaboModal: false,
        editLaboForm: {
          labnom: '',
          facno: null
        },
        labos: [],
        faculties : [],
        message: "",
        showMessage: false,
      };
    },
    components: {
      alert: Alert,
    },
    methods: {
      addLabo(payload) {
        const path = "http://localhost:5001/labos";
        axios
            .post(path, payload)
            .then(response => {
                // Assuming your Flask server sends the message in the response
                this.message = response.data.message;
                this.getlabos();
                this.showMessage = true;
            })
            .catch((error) => {
              console.log(error);
              console.log(payload);
              this.getlabos();
            });
      },
      get_faculty(id) {
        for(let elem of this.faculties) {
            if (elem.facno == id) {
                return elem.facnom;
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
        this.toggleAddLaboModal();
 
        const payload = {
          labnom: this.addLaboForm.labnom,
          facno: this.addLaboForm.facno,
        };
        this.addLabo(payload);
        this.initForm();
      },
      initForm() {
        this.addLaboForm.facno = null ;
        this.addLaboForm.labnom = "";
        this.editLaboForm.facno = null;
        this.editLaboForm.labnom = "";
      },
      toggleAddLaboModal() {
        const body = document.querySelector("body");
        this.activeAddLaboModal = !this.activeAddLaboModal;
        if (this.activeAddLaboModal) {
          body.classList.add("modal-open");
        } else {
          body.classList.remove("modal-open");
        }
      },
      toggleEditLaboModal(Labo) {
        if (Labo) {
          this.editLaboForm = Labo;
        }
        const body = document.querySelector("body");
        this.activeEditLaboModal = !this.activeEditLaboModal;
        if (this.activeEditLaboModal) {
          body.classList.add("modal-open");
        } else {
          body.classList.remove("modal-open");
        }
      },
      handleEditSubmit() {
        this.toggleEditLaboModal(null);
        let read = false;
        if (this.editLaboForm.read) read = true;
        const payload = {
          facno: this.editLaboForm.facno,
          labnom: this.editLaboForm.labnom,
        };
        this.updateLabo(payload, this.editLaboForm.labno);
      },
      updateLabo(payload, LabID) {
        const path = `http://localhost:5001/labos/${LabID}`;
        axios.put(path, payload)
            .then(() => {
              this.getlabos();
              this.message = 'Labo updated!';
              this.showMessage = true;
            })
            .catch((error) => {
              console.error(error);
              this.getlabos();
            });
      },
      handleEditCancel() {
        this.toggleEditLaboModal(null);
        this.initForm();
        this.getlabos(); // why?
      },
      handleDeleteLabo(Labo) {
        this.removeLabo(Labo.labno);
      },
      removeLabo(LaboID) {
        const path = `http://localhost:5001/labos/${LaboID}`;
        axios.delete(path)
            .then(() => {
              this.getlabos();
              this.message = 'Labo removed!';
              this.showMessage = true;
            })
            .catch((error) => {
              console.error(error);
              this.getlabos();
            });
      },
    },
    created() {
      this.getlabos();
      this.getfaculties()
    },
  };
  </script>
  