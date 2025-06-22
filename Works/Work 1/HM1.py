import time

def checkElementInSet(element, exmplSet):
    startingTime = time.perf_counter()
    isPresent = element in exmplSet
    endingTime = time.perf_counter()

    timeFormul = endingTime - startingTime
    return (isPresent, timeFormul)

if __name__ == "__main__":
    M = int(input('Введите кол-во нулей для заданного множества: '))
    exmplSet = set(range(1, 10**M+1))

    N = int(input('Введите количество элементов для поиска: '))
    elementsForTest = []
    c = 1
    for i in range(N):
        inpElem = int(input(f'Элемент {c}: '))
        elementsForTest.append(inpElem)
        c += 1

    print()

    for elem in elementsForTest:
        result, timeTaken = checkElementInSet(elem, exmplSet)
        print(f"Элемент {elem}: {'найден' if result else 'не найден'}")
        print(f"Время поиска: {timeTaken:.10f} секунд\n")