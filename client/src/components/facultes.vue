<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Facultés</h1>
          <hr/>
          <br/><br/>
          <alert v-if="showMessage" :message="message"></alert>
          <button
              class="btn btn-success btn-sm"
              type="button"
              @click="toggleAddFacultyModal">
            Ajouter une faculté
          </button>
          <br/><br/>
          <table class="table table-hover">
            <thead>
            <tr>
              <th scope="col">Nom de la faculté</th>
              <th scope="col">Adresse</th>
              <th scope="col">Libelle</th>
              <th></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(Faculty, index) in faculties" :key="index">
              <td>{{ Faculty.facnom }}</td>
              <td>{{ Faculty.adresse }}</td>
              <td>{{ Faculty.libelle }}</td>

              <td>
                <div class="btn-group" role="group">
                  <button
                      class="btn btn-warning btn-sm"
                      type="button"
                      @click="toggleEditFacultyModal(Faculty)">
                    Update
                  </button>
                  <button
                      class="btn btn-danger btn-sm"
                      type="button"
                      @click="handleDeleteFaculty(Faculty)">
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
    <!-- add new Faculty modal -->
    <div
        ref="addFacultyModal"
        :class="{ show: activeAddFacultyModal, 'd-block': activeAddFacultyModal }"
        class="modal fade"
        role="dialog"
        tabindex="-1">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new Faculty</h5>
            <button
                aria-label="Close"
                class="close"
                data-dismiss="modal"
                type="button"
                @click="toggleAddFacultyModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label class="form-label" for="addFacultyTitle">Nom de la faculté:</label>
                <input
                    id="addFacultyName"
                    v-model="addFacultyForm.facnom"
                    class="form-control"
                    placeholder="Entrez le nom de la faculté"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-label" for="addFacultyAdresse">L'adresse de la faculté:</label>
                <input
                    id="addFacultyAdresse"
                    v-model="addFacultyForm.adresse"
                    class="form-control"
                    placeholder="Entrez l'adresse"
                    type="text"/>
              </div>
              <div class="mb-3">
                <label class="form-check-label" for="addFacultyLibelle">Libelle de la faculté</label>
                <input
                    id="addFacultyLibelle"
                    v-model="addFacultyForm.libelle"
                    class="form-control"
                    type="text"/>
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
    <div v-if="activeAddFacultyModal" class="modal-backdrop fade show"></div>
    <!-- edit Faculty modal -->
    <div
        ref="editFacultyModal"
        :class="{ show: activeEditFacultyModal, 'd-block': activeEditFacultyModal }"
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
                @click="toggleEditFacultyModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label class="form-label" for="editFacultyName">Nom de la faculté:</label>
                <input
                    id="editFacultyName"
                    v-model="editFacultyForm.facnom"
                    class="form-control"
                    placeholder="Enter the new faculty name"
                    type="text">
              </div>
              <div class="mb-3">
                <label class="form-label" for="editFacultylibelle">Libelle:</label>
                <input
                    id="editFacultyLibelle"
                    v-model="editFacultyForm.libelle"
                    class="form-control"
                    placeholder="Enter Libelle"
                    type="text">
              </div>
              <div class="mb-3">
                <label class="form-label" for="editFacultyAdresse">Adresse:</label>
                <input
                    id="editFacultyAdresse"
                    v-model="editFacultyForm.adresse"
                    class="form-control"
                    placeholder="Entrez la nouvelle adresse"
                    type="text">
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
    <div v-if="activeEditFacultyModal" class="modal-backdrop fade show"></div>
  </template>
  
  <script>
  import axios from "axios";
  import Alert from "./Alert.vue";
  
  export default {
    data() {
      return {
        activeAddFacultyModal: false,
        addFacultyForm: {
          facnom: "",
          libelle: "",
          adresse: "",
        },
        activeEditFacultyModal: false,
        editFacultyForm: {
          id: '',
          title: '',
          author: '',
          read: [],
        },
        faculties: [],
        message: "",
        showMessage: false,
      };
    },
    components: {
      alert: Alert,
    },
    methods: {
      addFaculty(payload) {
        const path = "http://localhost:5001/faculties";
        axios
            .post(path, payload)
            .then(response => {
                // Assuming your Flask server sends the message in the response
                this.message = response.data.message;
                this.getfaculties();
                this.showMessage = true;
                console.log(response.data);
            })
            .catch((error) => {
              console.log(error);
              console.log(payload);
              this.getfaculties();
            });
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
      handleAddReset() {
        this.initForm();
      },
      handleAddSubmit() {
        this.toggleAddFacultyModal();
 
        const payload = {
          facnom: this.addFacultyForm.facnom,
          libelle: this.addFacultyForm.libelle,
          adresse : this.addFacultyForm.adresse // property shorthand
        };
        this.addFaculty(payload);
        this.initForm();
      },
      initForm() {
        this.addFacultyForm.facnom = "";
        this.addFacultyForm.adresse = "";
        this.addFacultyForm.libelle ="" ;
        this.editFacultyForm.facnom = "";
        this.editFacultyForm.adresse = "";
        this.editFacultyForm.libelle = "";
      },
      toggleAddFacultyModal() {
        const body = document.querySelector("body");
        this.activeAddFacultyModal = !this.activeAddFacultyModal;
        if (this.activeAddFacultyModal) {
          body.classList.add("modal-open");
        } else {
          body.classList.remove("modal-open");
        }
      },
      toggleEditFacultyModal(Faculty) {
        if (Faculty) {
          this.editFacultyForm = Faculty;
        }
        const body = document.querySelector("body");
        this.activeEditFacultyModal = !this.activeEditFacultyModal;
        if (this.activeEditFacultyModal) {
          body.classList.add("modal-open");
        } else {
          body.classList.remove("modal-open");
        }
      },
      handleEditSubmit() {
        this.toggleEditFacultyModal(null);
        let read = false;
        if (this.editFacultyForm.read) read = true;
        const payload = {
          facnom: this.editFacultyForm.facnom,
          libelle: this.editFacultyForm.libelle,
          adresse: this.editFacultyForm.adresse,
        };
        this.updateFaculty(payload, this.editFacultyForm.facno);
      },
      updateFaculty(payload, FacultyID) {
        const path = `http://localhost:5001/faculties/${FacultyID}`;
        axios.put(path, payload)
            .then(() => {
              this.getfaculties();
              this.message = 'Faculty updated!';
              this.showMessage = true;
            })
            .catch((error) => {
              console.error(error);
              this.getfaculties();
            });
      },
      handleEditCancel() {
        this.toggleEditFacultyModal(null);
        this.initForm();
        this.getfaculties(); // why?
      },
      handleDeleteFaculty(Faculty) {
        this.removeFaculty(Faculty.facno);
      },
      removeFaculty(FacultyID) {
        const path = `http://localhost:5001/faculties/${FacultyID}`;
        axios.delete(path)
            .then(() => {
              this.getfaculties();
              this.message = 'Faculty removed!';
              this.showMessage = true;
            })
            .catch((error) => {
              console.error(error);
              this.getfaculties();
            });
      },
    },
    created() {
      this.getfaculties();
    },
  };
  </script>
  