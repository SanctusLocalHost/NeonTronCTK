#!/usr/bin/env python3
"""
CustomTkinter Theme Showcase - Full HD Edition
Demonstração visual completa em tela única otimizada para 1920x1080
Autor: Sistema de demonstração profissional
Python 3.8+
"""

import customtkinter as ctk
import json
from typing import Dict, Any, List, Tuple
import tkinter as tk
from tkinter import messagebox

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ThemeManager:
    """Gerenciador de temas customizados para CustomTkinter"""
    
    def __init__(self, theme_data: Dict[str, Any]):
        self.theme_data = theme_data
        self.current_mode = 1  # 0 = light, 1 = dark
        
    def apply_theme_to_widget(self, widget: Any, widget_type: str) -> None:
        """
        Aplica as configurações do tema a um widget específico
        
        Args:
            widget: Widget CustomTkinter para aplicar o tema
            widget_type: Tipo do widget (ex: CTkButton, CTkLabel)
        """
        if widget_type not in self.theme_data:
            return
            
        config = self.theme_data[widget_type]
        
        for key, value in config.items():
            try:
                if isinstance(value, list) and len(value) == 2:
                    # Valores com modo light/dark
                    widget.configure(**{key: value[self.current_mode]})
                else:
                    # Valores únicos
                    widget.configure(**{key: value})
            except:
                # Ignora configurações incompatíveis
                pass
    
    def toggle_mode(self) -> str:
        """Alterna entre modo light e dark"""
        self.current_mode = 1 - self.current_mode
        mode = "light" if self.current_mode == 0 else "dark"
        ctk.set_appearance_mode(mode)
        return mode


class ThemeShowcaseFullHD(ctk.CTk):
    """Aplicação otimizada para exibição em tela cheia Full HD"""
    
    def __init__(self):
        super().__init__()
        
        # Carrega o tema customizado
        self.theme_data = {
            "CTk": {"fg_color": ["#EAEAEA", "#000000"]},
            "CTkToplevel": {"fg_color": ["#EAEAEA", "#000000"]},
            "CTkFrame": {
                "corner_radius": 6,
                "border_width": 0,
                "fg_color": ["#DCDCDC", "#0A0A0A"],
                "top_fg_color": ["#C8C8C8", "#050505"],
                "border_color": ["#B0B0B0", "#007080"]
            },
            "CTkButton": {
                "corner_radius": 6,
                "border_width": 0,
                "fg_color": ["#00D1D1", "#00D1D1"],
                "selected_fg_color": ["#00c6c7", "#00A0A0"],
                "hover_color": ["#00A0A0", "#00A0A0"],
                "text_color": ["#001010", "#001010"],
                "text_color_disabled": ["#007080", "#007080"],
                "fg_color_disabled": ["#A0E0E8", "#00404A"]
            },
            "CTkLabel": {
                "corner_radius": 0,
                "fg_color": "transparent",
                "text_color": ["#424242", "#00D1D1"]
            },
            "CTkEntry": {
                "corner_radius": 6,
                "border_width": 1,
                "fg_color": ["#FFFFFF", "#1A1A1A"],
                "border_color": ["#B0B0B0", "#00D1D1"],
                "text_color": ["#333333", "#E0E0E0"],
                "placeholder_text_color": ["#9E9E9E", "#00A0A0"]
            },
            "CTkCheckBox": {
                "corner_radius": 6,
                "border_width": 2,
                "fg_color": ["#757575", "#00D1D1"],
                "border_color": ["#BDBDBD", "#00A0A0"],
                "hover_color": ["#8A8A8A", "#00A0A0"],
                "checkmark_color": ["#FFFFFF", "#001010"],
                "text_color": ["#424242", "#00D1D1"],
                "text_color_disabled": ["#BDBDBD", "#007080"]
            },
            "CTkSwitch": {
                "corner_radius": 1000,
                "border_width": 2,
                "button_length": 0,
                "fg_color": ["#D0D0D0", "#505050"],
                "progress_color": ["#00c6c7", "#00D1D1"],
                "button_color": ["#BDBDBD", "#A0D8E0"],
                "button_hover_color": ["#ADADAD", "#00A0A0"],
                "text_color": ["#424242", "#00D1D1"],
                "text_color_disabled": ["#BDBDBD", "#007080"]
            },
            "CTkRadioButton": {
                "corner_radius": 1000,
                "border_width_checked": 6,
                "border_width_unchecked": 2,
                "fg_color": ["#757575", "#00D1D1"],
                "border_color": ["#BDBDBD", "#00A0A0"],
                "hover_color": ["#8A8A8A", "#00A0A0"],
                "text_color": ["#424242", "#00D1D1"],
                "text_color_disabled": ["#BDBDBD", "#007080"]
            },
            "CTkProgressBar": {
                "corner_radius": 1000,
                "border_width": 0,
                "fg_color": ["#D0D0D0", "#505050"],
                "progress_color": ["#757575", "#00D1D1"],
                "border_color": ["#B0B0B0", "#007080"]
            },
            "CTkSlider": {
                "corner_radius": 1000,
                "button_corner_radius": 1000,
                "border_width": 3,
                "button_length": 0,
                "fg_color": ["#D0D0D0", "#505050"],
                "progress_color": ["#757575", "#00D1D1"],
                "button_color": ["#757575", "#00D1D1"],
                "button_hover_color": ["#8A8A8A", "#00A0A0"]
            },
            "CTkOptionMenu": {
                "corner_radius": 6,
                "fg_color": ["#C8C8C8", "#00D1D1"],
                "button_color": ["#BDBDBD", "#00A0A0"],
                "button_hover_color": ["#ADADAD", "#007080"],
                "text_color": ["#333333", "#001010"],
                "text_color_disabled": ["#9E9E9E", "#007080"]
            },
            "CTkComboBox": {
                "corner_radius": 6,
                "border_width": 1,
                "fg_color": ["#FFFFFF", "#1A1A1A"],
                "border_color": ["#B0B0B0", "#00D1D1"],
                "button_color": ["#C8C8C8", "#00D1D1"],
                "button_hover_color": ["#BDBDBD", "#00A0A0"],
                "text_color": ["#333333", "#E0E0E0"],
                "text_color_disabled": ["#9E9E9E", "#007080"]
            },
            "CTkScrollbar": {
                "corner_radius": 1000,
                "border_spacing": 4,
                "fg_color": "transparent",
                "button_color": ["#BDBDBD", "#505050"],
                "button_hover_color": ["#ADADAD", "#00A0A0"]
            },
            "CTkSegmentedButton": {
                "corner_radius": 6,
                "border_width": 1,
                "fg_color": ["#DCDCDC", "#1A1A1A"],
                "selected_color": ["#00c6c7", "#00D1D1"],
                "selected_hover_color": ["#00A0A0", "#00A0A0"],
                "unselected_color": ["#DCDCDC", "#1A1A1A"],
                "unselected_hover_color": ["#C8C8C8", "#2A2A2A"],
                "text_color": ["#001010", "#001010"],
                "text_color_disabled": ["#BDBDBD", "#007080"]
            },
            "CTkTextbox": {
                "corner_radius": 6,
                "border_width": 1,
                "fg_color": ["#FFFFFF", "#0A0A0A"],
                "border_color": ["#B0B0B0", "#00D1D1"],
                "text_color": ["#333333", "#E0E0E0"],
                "scrollbar_button_color": ["#BDBDBD", "#505050"],
                "scrollbar_button_hover_color": ["#ADADAD", "#00A0A0"]
            }
        }
        
        self.theme_manager = ThemeManager(self.theme_data)
        self.widgets_list: List[Tuple[str, Any]] = []
        
        # Configuração da janela para Full HD
        self.title("NEON TRON CTK - Full HD")
        self.geometry("1920x1080")
        self.state('zoomed')  # Inicia maximizado no Windows
        
        # Aplica tema à janela principal
        self.theme_manager.apply_theme_to_widget(self, "CTk")
        
        # Cria a interface otimizada
        self.create_optimized_ui()
        
        # Aplica tema inicial
        self.apply_theme_to_all()
        
    def create_optimized_ui(self):
        """Cria interface otimizada para visualização em tela única"""
        
        # Container principal
        main_container = ctk.CTkFrame(self)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        self.widgets_list.append(("CTkFrame", main_container))
        
        # Header compacto
        self.create_compact_header(main_container)
        
        # Grid principal 3x3 para organizar seções
        content_grid = ctk.CTkFrame(main_container)
        content_grid.pack(fill="both", expand=True, pady=10)
        self.widgets_list.append(("CTkFrame", content_grid))
        
        # Configurar grid com pesos para distribuição uniforme
        for i in range(3):
            content_grid.grid_columnconfigure(i, weight=1, uniform="column")
            content_grid.grid_rowconfigure(i, weight=1, uniform="row")
        
        # Criar seções organizadas no grid
        self.create_buttons_section_compact(content_grid, 0, 0)
        self.create_input_section_compact(content_grid, 0, 1)
        self.create_selection_section_compact(content_grid, 0, 2)
        self.create_sliders_section_compact(content_grid, 1, 0)
        self.create_switches_section_compact(content_grid, 1, 1)
        self.create_display_section_compact(content_grid, 1, 2)
        self.create_advanced_section_compact(content_grid, 2, 0, colspan=3)
        
    def create_compact_header(self, parent):
        """Header compacto com título e controle de tema"""
        header_frame = ctk.CTkFrame(parent, height=60)
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)
        self.widgets_list.append(("CTkFrame", header_frame))
        
        # Título
        title = ctk.CTkLabel(
            header_frame,
            text="🎨 NEON TRON CTK - Full HD",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title.pack(side="left", padx=20)
        self.widgets_list.append(("CTkLabel", title))
        
        # Controle de tema
        theme_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        theme_frame.pack(side="right", padx=20)
        self.widgets_list.append(("CTkFrame", theme_frame))
        
        self.theme_label = ctk.CTkLabel(
            theme_frame,
            text="Modo Escuro",
            font=ctk.CTkFont(size=16)
        )
        self.theme_label.pack(side="left", padx=10)
        self.widgets_list.append(("CTkLabel", self.theme_label))
        
        theme_switch = ctk.CTkSwitch(
            theme_frame,
            text="",
            command=self.toggle_theme,
            width=60,
            height=30
        )
        theme_switch.pack(side="left")
        theme_switch.select()
        self.widgets_list.append(("CTkSwitch", theme_switch))
        
    def create_section_frame(self, parent, row, col, title, icon="", colspan=1):
        """Cria um frame de seção padronizado"""
        section_frame = ctk.CTkFrame(parent)
        section_frame.grid(row=row, column=col, columnspan=colspan, 
                          padx=10, pady=10, sticky="nsew")
        self.widgets_list.append(("CTkFrame", section_frame))
        
        # Título da seção
        title_frame = ctk.CTkFrame(section_frame, height=40)
        title_frame.pack(fill="x", padx=15, pady=(10, 5))
        self.widgets_list.append(("CTkFrame", title_frame))
        
        title_label = ctk.CTkLabel(
            title_frame,
            text=f"{icon} {title}",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title_label.pack(side="left")
        self.widgets_list.append(("CTkLabel", title_label))
        
        # Content frame
        content_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        return content_frame
        
    def create_buttons_section_compact(self, parent, row, col):
        """Seção de botões compacta"""
        content = self.create_section_frame(parent, row, col, "Botões", "🔘")
        
        buttons = [
            ("Normal", None, "normal", 0, 0),
            ("Hover Me", None, "normal", 0, 1),
            ("Desabilitado", None, "disabled", 1, 0),
            ("🚀 Ícone", None, "normal", 1, 1),
            ("Grande", ctk.CTkFont(size=16), "normal", 2, 0),
            ("Pequeno", ctk.CTkFont(size=11), "normal", 2, 1)
        ]
        
        for text, font, state, r, c in buttons:
            btn = ctk.CTkButton(
                content, text=text, font=font, state=state,
                width=140, height=35
            )
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="ew")
            self.widgets_list.append(("CTkButton", btn))
            
    def create_input_section_compact(self, parent, row, col):
        """Seção de inputs compacta"""
        content = self.create_section_frame(parent, row, col, "Entrada", "✏️")
        
        # Entry
        entry1 = ctk.CTkEntry(content, placeholder_text="Digite algo...", width=280)
        entry1.pack(pady=5)
        self.widgets_list.append(("CTkEntry", entry1))
        
        # Entry preenchido
        entry2 = ctk.CTkEntry(content, width=280)
        entry2.insert(0, "Texto preenchido")
        entry2.pack(pady=5)
        self.widgets_list.append(("CTkEntry", entry2))
        
        # ComboBox
        combo = ctk.CTkComboBox(
            content,
            values=["Opção 1", "Opção 2", "Opção 3"],
            width=280
        )
        combo.pack(pady=5)
        self.widgets_list.append(("CTkComboBox", combo))
        
        # TextBox menor
        textbox = ctk.CTkTextbox(content, width=280, height=120)
        textbox.insert("1.0", "Área de texto multilinha\ncom tema customizado\naplicado!")
        textbox.pack(pady=5)
        self.widgets_list.append(("CTkTextbox", textbox))
        
    def create_selection_section_compact(self, parent, row, col):
        """Seção de seleção compacta"""
        content = self.create_section_frame(parent, row, col, "Seleção", "☑️")
        
        # Checkboxes
        check_frame = ctk.CTkFrame(content, fg_color="transparent")
        check_frame.pack(side="left", fill="both", expand=True)
        
        checks = [
            ("Marcado", True, "normal"),
            ("Desmarcado", False, "normal"),
            ("Desabilitado", True, "disabled")
        ]
        
        for text, checked, state in checks:
            cb = ctk.CTkCheckBox(check_frame, text=text, state=state)
            if checked:
                cb.select()
            cb.pack(pady=5, anchor="w")
            self.widgets_list.append(("CTkCheckBox", cb))
        
        # Radio buttons
        radio_frame = ctk.CTkFrame(content, fg_color="transparent")
        radio_frame.pack(side="right", fill="both", expand=True)
        
        radio_var = tk.IntVar(value=1)
        for i, text in enumerate(["Opção 1", "Opção 2", "Opção 3"], 1):
            rb = ctk.CTkRadioButton(radio_frame, text=text, variable=radio_var, value=i)
            rb.pack(pady=5, anchor="w")
            self.widgets_list.append(("CTkRadioButton", rb))
            
        # Option Menu
        option_menu = ctk.CTkOptionMenu(
            content,
            values=["Menu 1", "Menu 2", "Menu 3"],
            width=280
        )
        option_menu.pack(pady=10)
        self.widgets_list.append(("CTkOptionMenu", option_menu))
        
    def create_sliders_section_compact(self, parent, row, col):
        """Seção de sliders e progress bars"""
        content = self.create_section_frame(parent, row, col, "Controles", "🎚️")
        
        # Progress bars com diferentes valores
        for i, value in enumerate([0.3, 0.6, 0.9]):
            pb = ctk.CTkProgressBar(content, width=280)
            pb.set(value)
            pb.pack(pady=8)
            self.widgets_list.append(("CTkProgressBar", pb))
            
        # Sliders
        for i in range(2):
            slider_frame = ctk.CTkFrame(content, fg_color="transparent")
            slider_frame.pack(pady=8, fill="x")
            
            slider = ctk.CTkSlider(slider_frame, from_=0, to=100, width=230)
            slider.set(25 + i * 50)
            slider.pack(side="left")
            self.widgets_list.append(("CTkSlider", slider))
            
            value_label = ctk.CTkLabel(slider_frame, text=f"{25 + i * 50}")
            value_label.pack(side="left", padx=10)
            self.widgets_list.append(("CTkLabel", value_label))
            
            def update_label(val, label=value_label):
                label.configure(text=f"{int(val)}")
            slider.configure(command=update_label)
            
    def create_switches_section_compact(self, parent, row, col):
        """Seção de switches"""
        content = self.create_section_frame(parent, row, col, "Switches", "🔀")
        
        switches_config = [
            ("Notificações", True, "normal"),
            ("Som do Sistema", False, "normal"),
            ("Modo Noturno Auto", True, "normal"),
            ("Sincronização", False, "normal"),
            ("Desabilitado", False, "disabled")
        ]
        
        for text, selected, state in switches_config:
            switch = ctk.CTkSwitch(content, text=text, state=state)
            if selected:
                switch.select()
            switch.pack(pady=8, anchor="w")
            self.widgets_list.append(("CTkSwitch", switch))
            
    def create_display_section_compact(self, parent, row, col):
        """Seção de display e frames especiais"""
        content = self.create_section_frame(parent, row, col, "Display", "🖼️")
        
        # Segmented button
        seg_button = ctk.CTkSegmentedButton(
            content,
            values=["Tab 1", "Tab 2", "Tab 3"],
            width=280
        )
        seg_button.pack(pady=10)
        seg_button.set("Tab 2")
        self.widgets_list.append(("CTkSegmentedButton", seg_button))
        
        # Frame com borda
        bordered_frame = ctk.CTkFrame(
            content,
            border_width=2,
            border_color=["#B0B0B0", "#007080"],
            height=100
        )
        bordered_frame.pack(fill="x", pady=10)
        bordered_frame.pack_propagate(False)
        self.widgets_list.append(("CTkFrame", bordered_frame))
        
        border_label = ctk.CTkLabel(
            bordered_frame,
            text="Frame com Borda\nCustomizada",
            font=ctk.CTkFont(size=14)
        )
        border_label.pack(expand=True)
        self.widgets_list.append(("CTkLabel", border_label))
        
        # Labels com diferentes estilos
        for text, size in [("Label Normal", 14), ("Label Grande", 18), ("Label Pequeno", 11)]:
            label = ctk.CTkLabel(content, text=text, font=ctk.CTkFont(size=size))
            label.pack(pady=5)
            self.widgets_list.append(("CTkLabel", label))
            
    def create_advanced_section_compact(self, parent, row, col, colspan):
        """Seção avançada ocupando toda a largura inferior"""
        content = self.create_section_frame(parent, row, col, "Showcase Avançado", "⚡", colspan)
        
        # Criar três colunas
        for i in range(3):
            column = ctk.CTkFrame(content, fg_color="transparent")
            column.pack(side="left", fill="both", expand=True, padx=10)
            
            if i == 0:
                # Coluna 1: Combinações de widgets
                combo_label = ctk.CTkLabel(column, text="Formulário Demo", font=ctk.CTkFont(size=14, weight="bold"))
                combo_label.pack(pady=5)
                self.widgets_list.append(("CTkLabel", combo_label))
                
                form_frame = ctk.CTkFrame(column)
                form_frame.pack(fill="x", pady=5)
                self.widgets_list.append(("CTkFrame", form_frame))
                
                # Mini formulário
                fields = ["Nome:", "Email:", "Senha:"]
                for idx, field in enumerate(fields):
                    label = ctk.CTkLabel(form_frame, text=field, width=80)
                    label.grid(row=idx, column=0, padx=5, pady=5, sticky="e")
                    self.widgets_list.append(("CTkLabel", label))
                    
                    entry = ctk.CTkEntry(form_frame, width=180)
                    if field == "Senha:":
                        entry.configure(show="*")
                    entry.grid(row=idx, column=1, padx=5, pady=5)
                    self.widgets_list.append(("CTkEntry", entry))
                    
            elif i == 1:
                # Coluna 2: Estados e variações
                states_label = ctk.CTkLabel(column, text="Estados dos Widgets", font=ctk.CTkFont(size=14, weight="bold"))
                states_label.pack(pady=5)
                self.widgets_list.append(("CTkLabel", states_label))
                
                # Botões em diferentes estados
                btn_states = [
                    ("✓ Sucesso", "#2ECC71"),
                    ("⚠ Aviso", "#F39C12"),
                    ("✗ Erro", "#E74C3C")
                ]
                
                for text, color in btn_states:
                    btn = ctk.CTkButton(column, text=text, fg_color=color, hover_color=color, width=200)
                    btn.pack(pady=5)
                    self.widgets_list.append(("CTkButton", btn))
                    
            else:
                # Coluna 3: Informações do tema
                info_label = ctk.CTkLabel(column, text="Informações do Tema", font=ctk.CTkFont(size=14, weight="bold"))
                info_label.pack(pady=5)
                self.widgets_list.append(("CTkLabel", info_label))
                
                info_text = ctk.CTkTextbox(column, width=250, height=150)
                info_text.insert("1.0", 
                    "🎨 Tema Customizado Aplicado\n\n"
                    "✓ Cores principais: #00D1D1\n"
                    "✓ Modo Light/Dark dinâmico\n"
                    "✓ Bordas arredondadas: 6px\n"
                    "✓ Hover effects customizados\n"
                    "✓ Estados disabled incluídos\n\n"
                    "Todos os widgets CTk suportados!"
                )
                info_text.configure(state="disabled")
                info_text.pack(pady=5)
                self.widgets_list.append(("CTkTextbox", info_text))
                
    def toggle_theme(self):
        """Alterna entre modo claro e escuro"""
        mode = self.theme_manager.toggle_mode()
        self.theme_label.configure(text="Modo Claro" if mode == "light" else "Modo Escuro")
        self.apply_theme_to_all()
        
    def apply_theme_to_all(self):
        """Aplica o tema a todos os widgets"""
        for widget_type, widget in self.widgets_list:
            try:
                self.theme_manager.apply_theme_to_widget(widget, widget_type)
            except:
                pass
                
        self.theme_manager.apply_theme_to_widget(self, "CTk")
        self.update()


def main():
    """Função principal do showcase"""
    try:
        app = ThemeShowcaseFullHD()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao iniciar:\n{str(e)}")


if __name__ == "__main__":
    main()