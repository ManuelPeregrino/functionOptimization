import random
import math

class GeneratePopulation:
    def __init__(self):
        
        # This class will generate each individual using the given range when called.
        # generatePopulation(): This function will, as i'ts name suggests, generate a population with individuals formated as bits within a given range.
        # generateIndividual(): This is an auxiliary function for generating each individual in bit format.
        # getBits(): This is an auxiliary generic function for obtaining the bits of a given number.
        # getBitEstimate(): This is an auxiliary function for getting the estimate of bits used by the system.
        # getSystemResolution(): This is an auxiliary generic function for estimating the system resolution.
        # getIndividualValue(): This is an auxiliary generic function for converting an array of binaries into integer values.
        # getPopulationValue(): This is an auxiliary generic function for returning the population values converted into integer values.
        #

        #Comment section for testing parameters:
        #self.TestGeneration=self.generatePopulation(5,0,15,0.1)
        #self.TestConvertion=self.getPopulationValue(self.TestGeneration)
        #print(self.TestConvertion)
        
        pass

    def generatePopulation(self, initialPopulation, minimum, maximum, referenceResolution):
        return [self.generateIndividual(self.getBits(minimum, maximum, referenceResolution), self.getBitEstimate(minimum, maximum, referenceResolution)) for i in range(initialPopulation)]
    
    def generateIndividual(self, numerosPosibles, bits):
        return [int(digit) for digit in bin(random.randint(0, numerosPosibles))[2:].zfill(bits)]
            
    def getBits(self, mini, maxi, referenceResolution):
        bitTotal = self.getBitEstimate(mini, maxi, referenceResolution)
        bitEstimate = 2**bitTotal - 1
        return bitEstimate%16
    
    def getBitEstimate(self, mini, maxi, referenceResolution):
        referenceResolution = referenceResolution
        bitRange = maxi-mini
        bitPoints = bitRange/referenceResolution + 1
        bitTotal = math.ceil(math.log2(bitPoints))
        return bitTotal
    
    def getSystemResolution(self, mini, maxi, bitEstimate):
        bitRange = int(maxi)-int(mini)
        systemResolution = bitRange/bitEstimate
        return systemResolution
    
    def getIndividualValue(self, individual):
        res = int("".join(str(x) for x in individual), 2)
        # printing result
        return res

    def getPopulationValue(self, population):
        convertedIndividuals = []
        for individual in population:
            convertedIndividuals.append(self.getIndividualValue(individual))
        return convertedIndividuals


#Test for class:
#GeneratePopulation()