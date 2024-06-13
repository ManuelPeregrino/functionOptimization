import tkinter as tk
from tkinter import ttk

class ParameterForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Parameter Form")

        # Labels and Entries for each parameter
        self.create_label_entry("Initial Population", 0)
        self.create_label_entry("Population Limit", 1)
        self.create_label_entry("Mutation Probability", 2)
        self.create_label_entry("Crossover Probability", 3)
        self.create_label_entry("Genome Mutation Probability", 4)
        self.create_label_entry("Generations", 5)
        self.create_label_entry("Reference Resolution", 6)
        self.create_label_entry("Graph Range Min", 7)
        self.create_label_entry("Graph Range Max", 8)

        # Behavior ComboBox
        behavior_label = tk.Label(self, text="Behavior")
        behavior_label.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
        self.behavior = ttk.Combobox(self, values=["maximize", "minimize"])
        self.behavior.grid(row=9, column=1, padx=10, pady=5)
        self.behavior.set("maximize")  # Default value

        # Submit Button
        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=10, columnspan=2, pady=10)

    def create_label_entry(self, label_text, row):
        label = tk.Label(self, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(self)
        entry.grid(row=row, column=1, padx=10, pady=5)
        setattr(self, label_text.replace(" ", "").lower(), entry)

    def submit(self):
        self.initialPopulation = self.initialpopulation.get()
        self.populationLimit = self.populationlimit.get()
        self.mutationProbability = self.mutationprobability.get()
        self.crossoverProbabilty = self.crossoverprobability.get()
        self.genomeMutationProbability = self.genomemutationprobability.get()
        self.generations = self.generations.get()
        self.referenceResolution = self.referenceresolution.get()
        self.graphRangeMin = self.graphrangemin.get()
        self.graphRangeMax = self.graphrangemax.get()
        self.Behavior = self.behavior.get()
        
        # You can add more actions here, e.g., print values or validate the input
        print("Form Submitted with the following values:")
        print(f"Initial Population: {self.initialPopulation}")
        print(f"Population Limit: {self.populationLimit}")
        print(f"Mutation Probability: {self.mutationProbability}")
        print(f"Crossover Probability: {self.crossoverProbabilty}")
        print(f"Genome Mutation Probability: {self.genomeMutationProbability}")
        print(f"Generations: {self.generations}")
        print(f"Reference Resolution: {self.referenceResolution}")
        print(f"Graph Range Min: {self.graphRangeMin}")
        print(f"Graph Range Max: {self.graphRangeMax}")
        print(f"Behavior: {self.Behavior}")

if __name__ == "__main__":
    app = ParameterForm()
    app.mainloop()
