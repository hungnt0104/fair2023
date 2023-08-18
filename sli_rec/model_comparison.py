import matplotlib.pyplot as plt

# Sample data (sli_rec_adaptive and lstm)
sli_rec_adaptive = [0.617985767562, 0.64242686958, 0.692616884125, 0.705777799657, 0.728963106899, 0.721046962617, 0.74148181798, 0.748687875769, 0.762605226176, 0.761238406609, 0.770895428279, 0.777211587371, 0.780660916769, 0.797613405814, 0.793574274069, 0.801802742997, 0.816190471291, 0.812014265237, 0.815104266139, 0.820722410195, 0.819471052594, 0.825274078201, 0.831776197974, 0.829808132543, 0.832270927092, 0.83546456131, 0.832155378441, 0.834532901153, 0.838757361538, 0.840083424131, 0.839396871158, 0.839336125548, 0.846892882763, 0.845661995443, 0.84574276392, 0.846032665348, 0.846508861635, 0.851875699658, 0.852211296275, 0.851440935925, 0.857275646838, 0.852576571245, 0.857368549702, 0.857566795363, 0.854569212297, 0.855963948936, 0.857066105845, 0.855502904007, 0.856548139377, 0.854403135019, 0.855385663968, 0.859387202721, 0.85470356802, 0.86303279419, 0.859436981123, 0.863503310629, 0.864715196358, 0.864545673049, 0.86538249927, 0.859007356631, 0.868320575104, 0.864993786965, 0.87095190826, 0.869302868729, 0.870921764596, 0.86824216624, 0.86786599285, 0.872843280163, 0.867337317537, 0.864395722785, 0.868027718921, 0.867557832245, 0.865776495876, 0.868018659097, 0.867235319836, 0.866677877527, 0.872193694715, 0.871102392298, 0.866934469943, 0.869387843873, 0.868878356796, 0.86797076992, 0.868977950501, 0.870398911522, 0.874102320594, 0.870055496972
                    ]  # Include all the values here
# Include all the values here
lstm = [0.622575875036, 0.63176322069, 0.65640615985, 0.697255167707, 0.709549192424, 0.707504737382, 0.726812199344, 0.736193041562, 0.746592291557, 0.744999887545, 0.751363500634, 0.754580792542, 0.756865299544, 0.771643215861, 0.75910118836, 0.774115635309, 0.775220944161, 0.783827475575, 0.787514098519, 0.791880370009, 0.791343623803, 0.793288267192, 0.796235257855, 0.79338207699, 0.798454346878, 0.801608879521, 0.799450999922, 0.803804701323, 0.800919830596, 0.803854050339, 0.804184508235, 0.806336128464, 0.810926996249, 0.810422373652, 0.811230073254, 0.810573534895, 0.808646633114, 0.815587212813, 0.817400313428, 0.81189589355, 0.819107039885, 0.818324608272, 0.823889424289, 0.821257721292,
        0.821047104488, 0.812584905966, 0.818693470754, 0.82356157942, 0.818425239587, 0.822455176146, 0.822536911037, 0.820221518868, 0.818959779636, 0.829291083356, 0.821990400207, 0.831570772343, 0.826849662701, 0.827894395081, 0.83156953312, 0.82139523618, 0.831066628984, 0.83374236357, 0.837535093397, 0.830776146796, 0.832112966067, 0.837835567787, 0.82688272832, 0.838752073853, 0.833015210006, 0.829996667205, 0.830362740362, 0.835269235392, 0.829466518973, 0.830773540016, 0.830759617273, 0.832147409721, 0.834242766549, 0.833529287193, 0.832262061071, 0.833804681475, 0.837871383294, 0.836907056513, 0.828440654903, 0.835033347474, 0.835776090763, 0.83308198923]

x_values = range(1, len(sli_rec_adaptive) + 1)

# Create the plot and plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(x_values, sli_rec_adaptive, label='sli_rec_adaptive',
         color='blue', linestyle='-', marker='o')
plt.plot(x_values, lstm, label='lstm', color='red', linestyle='-', marker='o')

# Add labels and title
plt.xlabel('Epochs')
plt.ylabel('AUC')
plt.title('AUC Comparison between sli_rec_adaptive and lstm')

# Add a grid for better visibility
plt.grid(True)

# Add a legend to differentiate between sli_rec_adaptive and lstm
plt.legend()

# Show the plot
plt.tight_layout()  # Adjust the layout for better spacing
plt.show()
