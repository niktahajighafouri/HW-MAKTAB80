from rest_framework.test import APITestCase
from rest_framework import status
from to_do_list.models import Tarefa


class TestTarefas(APITestCase):

    def setUp(self) -> None:
        self.tarefa = {"titulo": "Tarefa Teste", "data": "2022-12-26",
                       "concluida": False, "descricao": "Primeira tarefa"}

    def test_deve_retornar_status_code_200_no_metodo_get(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)

    def test_deve_incluir_conteudo_via_metodo_post(self):
        resposta = self.client.post("/tarefas/", self.tarefa)
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)

    def test_deve_retornar_o_mesmo_valor_de_contagem_dos_objetos_apos_inclusao(self):
        quantidade_inicial = Tarefa.objects.all().count()
        self.client.post("/tarefas/", self.tarefa)
        self.assertEqual(Tarefa.objects.all().count(), quantidade_inicial + 1)

    def test_deve_retornar_o_mesmo_conteudo_do_objeto_incluido(self):
        resposta_post = self.client.post("/tarefas/", self.tarefa)
        titulo = resposta_post.data["titulo"]

        resposta_get = self.client.get(f"/tarefas/{resposta_post.data['id']}/")

        self.assertEqual(resposta_get.status_code, status.HTTP_200_OK)
        self.assertEqual(titulo, resposta_get.data["titulo"])

    def test_deve_permitir_atualizar_o_conteudo_via_metodo_patch(self):
        resposta_post = self.client.post("/tarefas/", self.tarefa)

        patch = self.client.patch(f"/tarefas/{resposta_post.data['id']}/",
                                  {"titulo": "Nova Tarefa Teste"})
        self.assertEqual(patch.status_code, status.HTTP_200_OK)

        tarefa_atualizada = Tarefa.objects.get(id=resposta_post.data['id'])
        self.assertEqual(tarefa_atualizada.titulo, "Nova Tarefa Teste")

    def test_deve_permitir_deletar_um_objeto(self):
        resposta_post = self.client.post("/tarefas/", self.tarefa)

        delete = self.client.delete(f"/tarefas/{resposta_post.data['id']}/")
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_deve_retornar_zero_como_resultado_da_contagem_dos_objetos_apos_exclusao(self):
        resposta_post = self.client.post("/tarefas/", self.tarefa)
        quantidade_inicial = Tarefa.objects.all().count()

        # Quantidade inicial tem que ser maior que zero e igual a um,
        # pois uma tarefa acaba de ser adicionada
        self.assertGreater(quantidade_inicial, 0)
        self.assertEqual(quantidade_inicial, 1)

        self.client.delete(f"/tarefas/{resposta_post.data['id']}/")

        # Após a exclusão, é notório que a quantidade precisa ser zero
        self.assertEqual(Tarefa.objects.all().count(), 0)
