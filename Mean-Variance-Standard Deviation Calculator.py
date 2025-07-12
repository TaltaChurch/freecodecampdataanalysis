import numpy as np


testList = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")
        
    else:
        arr = np.array(list).reshape(3,3)
        
        
        
        result = {
        'mean': [arr.mean(axis=0).tolist(),arr.mean(axis=1).tolist(),arr.reshape(1,9).mean()],
        'variance': [arr.var(axis=0).tolist(),arr.var(axis=1).tolist(),arr.reshape(1,9).var()],
        'standard deviation': [arr.std(axis=0).tolist(),arr.std(axis=1).tolist(),arr.reshape(1,9).std()],
        'max': [arr.max(axis=0).tolist(),arr.max(axis=1).tolist(), arr.reshape(1,9).max()],
        'min': [arr.min(axis=0).tolist(),arr.min(axis=1).tolist(), arr.reshape(1,9).min()],
        'sum': [arr.sum(axis=0).tolist(),arr.sum(axis=1).tolist(), arr.reshape(1,9).sum()]
                
                
        }
        
        return result    
            
        
    
if __name__ == "__main__":
    print(calculate(testList))


