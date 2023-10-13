import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__

    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]

    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(midterm_kr, final_kr, label='Korean')
    plt.xlabel('Midterm Scores')
    plt.ylabel('Final Scores')
    plt.title('Midterm vs Final Scores (Korean)')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.scatter(midterm_en, final_en, label='English')
    plt.xlabel('Midterm Scores')
    plt.ylabel('Final Scores')
    plt.title('Midterm vs Final Scores (English)')
    plt.legend()
    plt.grid(True)

    plt.savefig('midterm_final_scatter.png')

    plt.figure(figsize=(8, 5))
    plt.hist(total_kr, bins=range(0, 101, 5), alpha=0.7, label='Korean', edgecolor='black')
    plt.hist(total_en, bins=range(0, 101, 5), alpha=0.7, label='English', edgecolor='black')
    plt.xlabel('Total Scores')
    plt.ylabel('Number of Students')
    plt.title('Total Scores Distribution')
    plt.legend()
    plt.grid(axis='y')
    plt.savefig('total_scores_histogram.png')

    plt.show()
