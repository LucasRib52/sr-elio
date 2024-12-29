from django.db import models
from clientes.models import RegistroClientes


# Registro de Atendimento
class RegistroAtendimento(models.Model):
    cliente = models.ForeignKey(RegistroClientes, on_delete=models.PROTECT, related_name="atendimentos")
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"Atendimento {self.id} - {self.cliente.name}"


# Histórico de Procedimentos
class HistoricoProcedimentos(models.Model):
    cliente = models.ForeignKey(RegistroClientes, on_delete=models.CASCADE, related_name="historico_procedimentos")
    procedimento = models.ForeignKey('Procedimentos', on_delete=models.CASCADE, related_name="historico_procedimentos")
    atendimento = models.ForeignKey('RegistroAtendimento', on_delete=models.CASCADE, related_name="procedimentos", blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.procedimento.nome} - {self.cliente.name}"


# Procedimentos
class Procedimentos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nome


# Agenda
class Agenda(models.Model):
    cliente = models.ForeignKey(RegistroClientes, on_delete=models.CASCADE, related_name="agendamentos")
    procedimento = models.ForeignKey(Procedimentos, on_delete=models.CASCADE, related_name="agendamentos")
    data_horario = models.DateTimeField()
    confirmado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['data_horario']

    def __str__(self):
        return f"Agendamento {self.id} - {self.cliente.name}"


# Relatórios
class Relatorios(models.Model):
    descricao = models.CharField(max_length=200)
    gerado_em = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='relatorios/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Relatório {self.descricao} - {self.gerado_em.strftime('%d/%m/%Y')}"
