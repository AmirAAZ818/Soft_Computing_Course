from RGA_Class import RGA
import theorem



rast_rga = RGA(target_function=theorem.rastrigin, function_dim=4, population=10, crossover_rate=0.8,
                   mutation_rate=0.005, max_gen=5, error=0.001,
                   function_config=[{'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12},
                                    {'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12}],
                   fitness_function=lambda x: 120 - theorem.rastrigin(x), run_bga=1,
                   plot_dir=r"E:\University of Kerman\Term 5\Soft Computing\HomeWorks\Soft_Computing_Course\BGA_HW_1\Plots")


rast_rga.Run()
