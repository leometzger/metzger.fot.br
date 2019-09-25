<template>
  <div class="site-section" data-aos="fade">
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-md-7">
          <div class="row">
            <div class="col-lg-8 mb-5">
              <form action="mailto:leonardo.metzger@outlook.com">
                <div class="row form-group">
                  <div class="col-md-6 mb-3 mb-md-0">
                    <label class="text-black" for="fname">Primeiro Nome</label>
                    <input type="text" id="fname" class="form-control" />
                  </div>
                  <div class="col-md-6">
                    <label class="text-black" for="lname">Último Nome</label>
                    <input type="text" id="lname" class="form-control" />
                  </div>
                </div>

                <div class="row form-group">
                  <div class="col-md-12">
                    <label class="text-black" for="email">Email</label>
                    <input type="email" id="email" class="form-control" />
                  </div>
                </div>

                <div class="row form-group">
                  <div class="col-md-12">
                    <label class="text-black" for="subject">Assunto</label>
                    <input type="subject" id="subject" class="form-control" />
                  </div>
                </div>

                <div class="row form-group">
                  <div class="col-md-12">
                    <label class="text-black" for="message">Mensagem</label>
                    <textarea
                      name="message"
                      id="message"
                      cols="30"
                      rows="7"
                      class="form-control"
                      placeholder="Write your notes or questions here..."
                    ></textarea>
                  </div>
                </div>

                <div class="row form-group">
                  <div class="col-md-12">
                    <input
                      type="submit"
                      value="Enviar"
                      class="btn btn-primary py-2 px-4 text-white"
                    />
                  </div>
                </div>
              </form>
            </div>
            <div class="col-lg-3 ml-auto">
              <div class="mb-3 bg-white">
                <p class="mb-0 font-weight-bold">Endereço</p>
                <p class="mb-4">Rua Marechal Floriano 79, São Bento do Sul, SC, Brasil</p>

                <p class="mb-0 font-weight-bold">Telefone</p>
                <p class="mb-4">
                  <a href="#">47 3634-0848</a>
                </p>

                <p class="mb-0 font-weight-bold">Endereço de Email</p>
                <p class="mb-0">
                  <a href="#">marcelo@metzger.fot.br</a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
