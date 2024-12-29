from django.db import models


# Registro de Clientes
class RegistroClientes(models.Model):
    name = models.CharField(max_length=400, verbose_name="Nome Completo")
    d_nasc = models.DateField(verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    telefone = models.CharField(max_length=12, verbose_name="Telefone")
    endereco = models.CharField(max_length=300, verbose_name="Endereço")
    email = models.EmailField(max_length=150, verbose_name="E-mail")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Histórico de Clientes
class HistoricoClientes(models.Model):
    cliente = models.ForeignKey(RegistroClientes, on_delete=models.CASCADE, related_name="historico")
    consulta_em = models.DateTimeField(auto_now_add=True, verbose_name="Consultado em")
    acao = models.CharField(max_length=255, verbose_name="Ação Realizada", blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta:
        ordering = ['-consulta_em']

    def __str__(self):
        return f"Histórico - {self.cliente.name} - {self.consulta_em.strftime('%d/%m/%Y %H:%M:%S')}"
