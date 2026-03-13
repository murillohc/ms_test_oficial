import { Component, signal, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ClientesService } from './services/clientes';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App implements OnInit {
  clientes = signal<any[]>([]);
  private mostrarInativosAtual = false;

  constructor(private clientesService: ClientesService) {}

  ngOnInit() {
    this.carregarClientes(false);
  }

  carregarClientes(mostrarInativos: boolean) {
    this.mostrarInativosAtual = mostrarInativos;
    this.clientesService
      .listar(mostrarInativos)
      .subscribe(data => {
        this.clientes.set(data);
      });
  }

  toggleFiltro() {
    this.mostrarInativosAtual = !this.mostrarInativosAtual;
    this.carregarClientes(this.mostrarInativosAtual);
  }

  inativar(id: number) {
    this.clientesService.inativar(id).subscribe(() => {
      this.carregarClientes(this.mostrarInativosAtual);
    });
  }

  reativar(id: number) {
    this.clientesService.reativar(id).subscribe(() => {
      this.carregarClientes(this.mostrarInativosAtual);
    });
  }

  get mostrandoInativos() {
    return this.mostrarInativosAtual;
  }
}
