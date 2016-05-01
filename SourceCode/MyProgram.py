'''
Created on Feb 2, 2016

@author: ABHISHEK PRASAD
'''
import sys
import copy
# Open a file
def evalenergy(gridres,plSym):
    plSymcount=0
    ploppSymcount=0
    for i in range(0,5):
        for j in range(0,5):
            if(gridres[i][j]==plSym):
                plSymcount=plSymcount+int(gridval[i][j])
            elif(gridres[i][j]!=plSym and gridres[i][j]!='*'):
                ploppSymcount=ploppSymcount+int(gridval[i][j])
    return (plSymcount-ploppSymcount)     

def TerminalTest(grid):
    for i in range(0,5):
        for j in range(0,5):
            if(grid[i][j]=='*'):
                return False;
    return True;

#MiniMax-Algorithm        
def MaxValue(gridres,plySym,depth,cutOffDep,r,c):
    if(int(depth)==int(cutOffDep) or TerminalTest(gridres)):
        return evalenergy(gridres, plySym)

    gridresult1 = [[0 for y in range(5)]for x in range(5)]
    gridresult1=copy.deepcopy(gridres)
    maxvalue=-sys.maxint-1
    for i in range(0,5):
        for j in range(0,5):
            if (gridres[i][j]=='*'):
                #if(i-1>-1 and j-1>-1 and i+1<5 and j+1<5):
                if((i-1>-1 and gridres[i-1][j]==plySym) or (i+1<5 and gridres[i+1][j]==plySym) or (j-1>-1 and gridres[i][j-1]==plySym) or (j+1<5 and gridres[i][j+1]==plySym)): 
                    gridresult1[i][j]=plySym
                    if(i-1>-1 and gridres[i-1][j]!=plySym and gridres[i-1][j]!='*'):
                        gridresult1[i-1][j]=plySym
                    if(i+1<5 and gridres[i+1][j]!=plySym and gridres[i+1][j]!='*'):
                        gridresult1[i+1][j]=plySym
                    if(j-1>-1 and gridres[i][j-1]!=plySym and gridres[i][j-1]!='*'):
                        gridresult1[i][j-1]=plySym
                    if(j+1<5 and gridres[i][j+1]!=plySym and gridres[i][j+1]!='*'):
                        gridresult1[i][j+1]=plySym
                else:
                    gridresult1[i][j]=plySym
                if debug==1:
                    if(maxvalue==(-sys.maxint-1)):
                        flog2.write("\n%s%s,%d,-Infinity"%(cval[c],rval[r],depth));            
                    else:
                        flog2.write("\n%s%s,%d,%d"%(cval[c],rval[r],depth,maxvalue));    
                energy=MinValue(gridresult1,plySym,depth+1,cutOffDep,i,j);
                if debug==1:
                    flog2.write("\n%s%s,%d,%d"%(cval[j],rval[i],depth+1,energy));
                if energy>maxvalue:
                    maxvalue=energy
                gridresult1=copy.deepcopy(gridres)
    return maxvalue
    
    
def MinValue(gridres,plySym,depth,cutOffDep,r,c):
    if(int(depth)==int(cutOffDep) or TerminalTest(gridres)):
        return evalenergy(gridres, plySym)
    
    gridresult1 = [[0 for y in range(5)]for x in range(5)]
    gridresult1=copy.deepcopy(gridres)
    if plySym=='X':
        oppSym='O'
    else:
        oppSym='X'    
    minvalue=sys.maxint
    for i in range(0,5):
        for j in range(0,5):
            if (gridres[i][j]=='*'):
                #if(i-1>-1 and j-1>-1 and i+1<5 and j+1<5):
                if((i-1>-1 and gridres[i-1][j]==oppSym) or (i+1<5 and gridres[i+1][j]==oppSym) or (j-1>-1 and gridres[i][j-1]==oppSym) or (j+1<5 and gridres[i][j+1]==oppSym)): 
                    gridresult1[i][j]=oppSym
                    if(i-1>-1 and gridres[i-1][j]!=oppSym and gridres[i-1][j]!='*'):
                        gridresult1[i-1][j]=oppSym
                    if(i+1<5 and gridres[i+1][j]!=oppSym and gridres[i+1][j]!='*'):
                        gridresult1[i+1][j]=oppSym
                    if(j-1>-1 and gridres[i][j-1]!=oppSym and gridres[i][j-1]!='*'):
                        gridresult1[i][j-1]=oppSym
                    if(j+1<5 and gridres[i][j+1]!=oppSym and gridres[i][j+1]!='*'):
                        gridresult1[i][j+1]=oppSym
                else:
                    gridresult1[i][j]=oppSym
                if debug==1:
                    if(minvalue==sys.maxint):
                        flog2.write("\n%s%s,%d,Infinity"%(cval[c],rval[r],depth));            
                    else:
                        flog2.write("\n%s%s,%d,%d"%(cval[c],rval[r],depth,minvalue));    
                energy=MaxValue(gridresult1,plySym,depth+1,cutOffDep,i,j);
                if debug==1:
                    flog2.write("\n%s%s,%d,%d"%(cval[j],rval[i],depth+1,energy));
                
                if energy<minvalue:
                    minvalue=energy
                gridresult1=copy.deepcopy(gridres)
    return minvalue
    
def MiniMaxDecision(gridresult,gridsym,playerSym,cutOffDep):
    rowmax=-1
    colmax=-1
    maxval=-sys.maxint-1
    if debug==1:
        flog2.write('\n')
        flog2.write("root,0,-Infinity");
    for i in range(0,5):
        for j in range(0,5):
            if (gridsym[i][j]=='*'):
                #if(i-1>-1 and j-1>-1 and i+1<5 and j+1<5):
                if((i-1>-1 and gridsym[i-1][j]==playerSym) or (i+1<5 and gridsym[i+1][j]==playerSym) or (j-1>-1 and gridsym[i][j-1]==playerSym) or (j+1<5 and gridsym[i][j+1]==playerSym)): 
                    gridresult[i][j]=playerSym
                    if(i-1>-1 and gridsym[i-1][j]!=playerSym and gridsym[i-1][j]!='*'):
                        gridresult[i-1][j]=playerSym
                    if(i+1<5 and gridsym[i+1][j]!=playerSym and gridsym[i+1][j]!='*'):
                        gridresult[i+1][j]=playerSym
                    if(j-1>-1 and gridsym[i][j-1]!=playerSym and gridsym[i][j-1]!='*'):
                        gridresult[i][j-1]=playerSym
                    if(j+1<5 and gridsym[i][j+1]!=playerSym and gridsym[i][j+1]!='*'):
                        gridresult[i][j+1]=playerSym
                else:
                    gridresult[i][j]=playerSym        
                energy=MinValue(gridresult,playerSym,1,cutOffDep,i,j);
                if debug==1:
                    flog2.write("\n%s%s,%d,%d"%(cval[j],rval[i],1,energy));
                if energy>maxval:
                    maxval=energy
                    rowmax=i
                    colmax=j
                if debug==1:
                    flog2.write("\nroot,0,%d" % maxval);
                gridresult=copy.deepcopy(gridsym)            
    
    
    i=rowmax
    j=colmax
    gridresult=copy.deepcopy(gridsym)
    if (rowmax==-1 or colmax==-1):
        print "Error in calculating row or column"
    elif((i-1>-1 and gridsym[i-1][j]==playerSym) or (i+1<5 and gridsym[i+1][j]==playerSym) or (j-1>-1 and gridsym[i][j-1]==playerSym) or (j+1<5 and gridsym[i][j+1]==playerSym)): 
        gridresult[i][j]=playerSym
        if(i-1>-1 and gridsym[i-1][j]!=playerSym and gridsym[i-1][j]!='*'):
            gridresult[i-1][j]=playerSym
        if(i+1<5 and gridsym[i+1][j]!=playerSym and gridsym[i+1][j]!='*'):
            gridresult[i+1][j]=playerSym
        if(j-1>-1 and gridsym[i][j-1]!=playerSym and gridsym[i][j-1]!='*'):
            gridresult[i][j-1]=playerSym
        if(j+1<5 and gridsym[i][j+1]!=playerSym and gridsym[i][j+1]!='*'):
            gridresult[i][j+1]=playerSym
    else:
        gridresult[i][j]=playerSym

    return gridresult

#AlphaBeta-Algorithm
def ABMaxValue(gridres,plySym,depth,cutOffDep,r,c,alph,beta1):
    if(int(depth)==int(cutOffDep) or TerminalTest(gridres)):
        maxvalue1=evalenergy(gridres, plySym)
        if debug==1:
            if(alph==-sys.maxint-1 and beta1==sys.maxint):
                flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,maxvalue1));
            elif(alph==-sys.maxint-1):
                flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,maxvalue1,beta1));
            elif(beta1==sys.maxint):
                flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,maxvalue1,alph));
            else:
                flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,maxvalue1,alph,beta1));

        return maxvalue1
    gridresult1 = [[0 for y in range(5)]for x in range(5)]
    gridresult1=copy.deepcopy(gridres)
    maxvalue=-sys.maxint-1
    for i in range(0,5):
        for j in range(0,5):
            if (gridres[i][j]=='*'):
                #if(i-1>-1 and j-1>-1 and i+1<5 and j+1<5):
                if((i-1>-1 and gridres[i-1][j]==plySym) or (i+1<5 and gridres[i+1][j]==plySym) or (j-1>-1 and gridres[i][j-1]==plySym) or (j+1<5 and gridres[i][j+1]==plySym)): 
                    gridresult1[i][j]=plySym
                    if(i-1>-1 and gridres[i-1][j]!=plySym and gridres[i-1][j]!='*'):
                        gridresult1[i-1][j]=plySym
                    if(i+1<5 and gridres[i+1][j]!=plySym and gridres[i+1][j]!='*'):
                        gridresult1[i+1][j]=plySym
                    if(j-1>-1 and gridres[i][j-1]!=plySym and gridres[i][j-1]!='*'):
                        gridresult1[i][j-1]=plySym
                    if(j+1<5 and gridres[i][j+1]!=plySym and gridres[i][j+1]!='*'):
                        gridresult1[i][j+1]=plySym
                else:
                    gridresult1[i][j]=plySym
                if debug==1:    
                    if(maxvalue==(-sys.maxint-1)):
                        if(alph==-sys.maxint-1 and beta1==sys.maxint):
                            flog2.write("\n%s%s,%d,-Infinity,-Infinity,Infinity"%(cval[c],rval[r],depth));
                        elif(alph==-sys.maxint-1):
                            flog2.write("\n%s%s,%d,-Infinity,-Infinity,%d"%(cval[c],rval[r],depth,beta1));
                        elif(beta1==sys.maxint):
                            flog2.write("\n%s%s,%d,-Infinity,%d,Infinity"%(cval[c],rval[r],depth,alph));
                        else:
                            flog2.write("\n%s%s,%d,-Infinity,%d,%d"%(cval[c],rval[r],depth,alph,beta1));                                
                    else:
                        if(alph==-sys.maxint-1 and beta1==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,maxvalue));
                        elif(alph==-sys.maxint-1):
                            flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,maxvalue,beta1));
                        elif(beta1==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,maxvalue,alph));
                        else:
                            flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,maxvalue,alph,beta1));
                energy=ABMinValue(gridresult1,plySym,depth+1,cutOffDep,i,j,alph,beta1);
                if energy>maxvalue:
                    maxvalue=energy
                if maxvalue>=beta1:
                    if debug==1:
                        if(alph==-sys.maxint-1 and beta1==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,maxvalue));
                        elif(alph==-sys.maxint-1):
                            flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,maxvalue,beta1));
                        elif(beta1==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,maxvalue,alph));
                        else:
                            flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,maxvalue,alph,beta1));
                    return maxvalue
                alph=max(alph,maxvalue)
                gridresult1=copy.deepcopy(gridres)
    if debug==1:
        if(alph==-sys.maxint-1 and beta1==sys.maxint):
            flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,maxvalue));
        elif(alph==-sys.maxint-1):
            flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,maxvalue,beta1));
        elif(beta1==sys.maxint):
            flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,maxvalue,alph));
        else:
            flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,maxvalue,alph,beta1));
    return maxvalue

def ABMinValue(gridres,plySym,depth,cutOffDep,r,c,alp,bta):
    if(int(depth)==int(cutOffDep) or TerminalTest(gridres)):
        minvalue1=evalenergy(gridres, plySym)
        if debug==1:
            if(alp==-sys.maxint-1 and bta==sys.maxint):
                flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,minvalue1));
            elif(alp==-sys.maxint-1):
                flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,minvalue1,bta));
            elif(bta==sys.maxint):
                flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,minvalue1,alp));
            else:
                flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,minvalue1,alp,bta)); 
        return minvalue1
    
    gridresult1 = [[0 for y in range(5)]for x in range(5)]
    gridresult1=copy.deepcopy(gridres)
    if plySym=='X':
        oppSym='O'
    else:
        oppSym='X'    
    minvalue=sys.maxint
    for i in range(0,5):
        for j in range(0,5):
            if (gridres[i][j]=='*'):
                if((i-1>-1 and gridres[i-1][j]==oppSym) or (i+1<5 and gridres[i+1][j]==oppSym) or (j-1>-1 and gridres[i][j-1]==oppSym) or (j+1<5 and gridres[i][j+1]==oppSym)): 
                    gridresult1[i][j]=oppSym
                    if(i-1>-1 and gridres[i-1][j]!=oppSym and gridres[i-1][j]!='*'):
                        gridresult1[i-1][j]=oppSym
                    if(i+1<5 and gridres[i+1][j]!=oppSym and gridres[i+1][j]!='*'):
                        gridresult1[i+1][j]=oppSym
                    if(j-1>-1 and gridres[i][j-1]!=oppSym and gridres[i][j-1]!='*'):
                        gridresult1[i][j-1]=oppSym
                    if(j+1<5 and gridres[i][j+1]!=oppSym and gridres[i][j+1]!='*'):
                        gridresult1[i][j+1]=oppSym
                else:
                    gridresult1[i][j]=oppSym
                if debug==1:
                    if(minvalue==sys.maxint):
                        if(alp==-sys.maxint-1 and bta==sys.maxint):
                            flog2.write("\n%s%s,%d,Infinity,-Infinity,Infinity"%(cval[c],rval[r],depth));
                        elif(alp==-sys.maxint-1):
                            flog2.write("\n%s%s,%d,Infinity,-Infinity,%d"%(cval[c],rval[r],depth,bta));
                        elif(bta==sys.maxint):
                            flog2.write("\n%s%s,%d,Infinity,%d,Infinity"%(cval[c],rval[r],depth,alp));
                        else:
                            flog2.write("\n%s%s,%d,Infinity,%d,%d"%(cval[c],rval[r],depth,alp,bta));                        
                    else:
                        if(alp==-sys.maxint-1 and bta==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,minvalue));
                        elif(alp==-sys.maxint-1):
                            flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,minvalue,bta));
                        elif(bta==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,minvalue,alp));
                        else:
                            flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,minvalue,alp,bta)); 
                energy=ABMaxValue(gridresult1,plySym,depth+1,cutOffDep,i,j,alp,bta);
                if energy<minvalue:
                    minvalue=energy
                if minvalue<=alp:
                    if debug==1:
                        if(alp==-sys.maxint-1 and bta==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,minvalue));
                        elif(alp==-sys.maxint-1):
                            flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,minvalue,bta));
                        elif(bta==sys.maxint):
                            flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,minvalue,alp));
                        else:
                            flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,minvalue,alp,bta));             

                    return minvalue
                bta=min(bta,minvalue)   
                gridresult1=copy.deepcopy(gridres)
    if debug==1:
        if(alp==-sys.maxint-1 and bta==sys.maxint):
            flog2.write("\n%s%s,%d,%d,-Infinity,Infinity"%(cval[c],rval[r],depth,minvalue));
        elif(alp==-sys.maxint-1):
            flog2.write("\n%s%s,%d,%d,-Infinity,%d"%(cval[c],rval[r],depth,minvalue,bta));
        elif(bta==sys.maxint):
            flog2.write("\n%s%s,%d,%d,%d,Infinity"%(cval[c],rval[r],depth,minvalue,alp));
        else:
            flog2.write("\n%s%s,%d,%d,%d,%d"%(cval[c],rval[r],depth,minvalue,alp,bta));             

    return minvalue

def AlphaBetaSearch(gridresult,gridsym,playerSym,cutOffDep):
    rowmax=-1
    colmax=-1
    maxval=-sys.maxint-1
    alpha=-sys.maxint-1
    beta=sys.maxint
    if debug==1:
        flog2.write('\n')
        flog2.write("root,0,-Infinity,-Infinity,Infinity");
    for i in range(0,5):
        for j in range(0,5):
            if (gridsym[i][j]=='*'):
                #if(i-1>-1 and j-1>-1 and i+1<5 and j+1<5):
                if((i-1>-1 and gridsym[i-1][j]==playerSym) or (i+1<5 and gridsym[i+1][j]==playerSym) or (j-1>-1 and gridsym[i][j-1]==playerSym) or (j+1<5 and gridsym[i][j+1]==playerSym)): 
                    gridresult[i][j]=playerSym
                    if(i-1>-1 and gridsym[i-1][j]!=playerSym and gridsym[i-1][j]!='*'):
                        gridresult[i-1][j]=playerSym
                    if(i+1<5 and gridsym[i+1][j]!=playerSym and gridsym[i+1][j]!='*'):
                        gridresult[i+1][j]=playerSym
                    if(j-1>-1 and gridsym[i][j-1]!=playerSym and gridsym[i][j-1]!='*'):
                        gridresult[i][j-1]=playerSym
                    if(j+1<5 and gridsym[i][j+1]!=playerSym and gridsym[i][j+1]!='*'):
                        gridresult[i][j+1]=playerSym
                else:
                    gridresult[i][j]=playerSym        
                energy=ABMinValue(gridresult,playerSym,1,cutOffDep,i,j,alpha,beta);
                if energy>maxval:
                    maxval=energy
                    rowmax=i
                    colmax=j
                if maxval>=beta:
                    i=rowmax
                    j=colmax
                    gridresult=copy.deepcopy(gridsym)
                    if (rowmax==-1 or colmax==-1):
                        print "Error in calculating row or column"
                    elif((i-1>-1 and gridsym[i-1][j]==playerSym) or (i+1<5 and gridsym[i+1][j]==playerSym) or (j-1>-1 and gridsym[i][j-1]==playerSym) or (j+1<5 and gridsym[i][j+1]==playerSym)): 
                        gridresult[i][j]=playerSym
                        if(i-1>-1 and gridsym[i-1][j]!=playerSym and gridsym[i-1][j]!='*'):
                            gridresult[i-1][j]=playerSym
                        if(i+1<5 and gridsym[i+1][j]!=playerSym and gridsym[i+1][j]!='*'):
                            gridresult[i+1][j]=playerSym
                        if(j-1>-1 and gridsym[i][j-1]!=playerSym and gridsym[i][j-1]!='*'):
                            gridresult[i][j-1]=playerSym
                        if(j+1<5 and gridsym[i][j+1]!=playerSym and gridsym[i][j+1]!='*'):
                            gridresult[i][j+1]=playerSym
                    else:
                        gridresult[i][j]=playerSym
                    if debug==1:
                        if(alpha==-sys.maxint-1 and beta==sys.maxint):
                            flog2.write("\nroot,0,%d,-Infinity,Infinity" % maxval);
                        elif(alpha==-sys.maxint-1):
                            flog2.write("\nroot,0,%d,-Infinity,%d" % (maxval,beta));
                        elif(beta==sys.maxint):
                            flog2.write("\nroot,0,%d,%d,Infinity" % (maxval,alpha));
                        else:
                            flog2.write("\nroot,0,%d,%d,%d" % (maxval,alpha,beta));    

                    return gridresult
                alpha=max(alpha,maxval)
                if debug==1:
                    if(alpha==-sys.maxint-1 and beta==sys.maxint):
                        flog2.write("\nroot,0,%d,-Infinity,Infinity" % maxval);
                    elif(alpha==-sys.maxint-1):
                        flog2.write("\nroot,0,%d,-Infinity,%d" % (maxval,beta));
                    elif(beta==sys.maxint):
                        flog2.write("\nroot,0,%d,%d,Infinity" % (maxval,alpha));
                    else:
                        flog2.write("\nroot,0,%d,%d,%d" % (maxval,alpha,beta));    
                gridresult=copy.deepcopy(gridsym)            
    
    
    i=rowmax
    j=colmax
    gridresult=copy.deepcopy(gridsym)
    if (rowmax==-1 or colmax==-1):
        print "Error in calculating row or column"
    elif((i-1>-1 and gridsym[i-1][j]==playerSym) or (i+1<5 and gridsym[i+1][j]==playerSym) or (j-1>-1 and gridsym[i][j-1]==playerSym) or (j+1<5 and gridsym[i][j+1]==playerSym)): 
        gridresult[i][j]=playerSym
        if(i-1>-1 and gridsym[i-1][j]!=playerSym and gridsym[i-1][j]!='*'):
            gridresult[i-1][j]=playerSym
        if(i+1<5 and gridsym[i+1][j]!=playerSym and gridsym[i+1][j]!='*'):
            gridresult[i+1][j]=playerSym
        if(j-1>-1 and gridsym[i][j-1]!=playerSym and gridsym[i][j-1]!='*'):
            gridresult[i][j-1]=playerSym
        if(j+1<5 and gridsym[i][j+1]!=playerSym and gridsym[i][j+1]!='*'):
            gridresult[i][j+1]=playerSym
    else:
        gridresult[i][j]=playerSym

    return gridresult

def GreedyBestFirst(gridresult,gridsym,playerSymb):
    rowmax=-1
    colmax=-1
    maxval=-sys.maxint-1
    for i in range(0,5):
        for j in range(0,5):
            if (gridsym[i][j]=='*'):
                #if(i-1>-1 and j-1>-1 and i+1<5 and j+1<5):
                if((i-1>-1 and gridsym[i-1][j]==playerSymb) or (i+1<5 and gridsym[i+1][j]==playerSymb) or (j-1>-1 and gridsym[i][j-1]==playerSymb) or (j+1<5 and gridsym[i][j+1]==playerSymb)): 
                    gridresult[i][j]=playerSymb
                    if(i-1>-1 and gridsym[i-1][j]!=playerSymb and gridsym[i-1][j]!='*'):
                        gridresult[i-1][j]=playerSymb
                    if(i+1<5 and gridsym[i+1][j]!=playerSymb and gridsym[i+1][j]!='*'):
                        gridresult[i+1][j]=playerSymb
                    if(j-1>-1 and gridsym[i][j-1]!=playerSymb and gridsym[i][j-1]!='*'):
                        gridresult[i][j-1]=playerSymb
                    if(j+1<5 and gridsym[i][j+1]!=playerSymb and gridsym[i][j+1]!='*'):
                        gridresult[i][j+1]=playerSymb
                else:
                    gridresult[i][j]=playerSymb        
                energy=evalenergy(gridresult,playerSymb);
                if energy>maxval:
                    maxval=energy
                    rowmax=i
                    colmax=j
                gridresult=copy.deepcopy(gridsym)            
    
    
    i=rowmax
    j=colmax
    gridresult=copy.deepcopy(gridsym)
    if (rowmax==-1 or colmax==-1):
        print "Error in calculating row or column"
    elif((i-1>-1 and gridsym[i-1][j]==playerSymb) or (i+1<5 and gridsym[i+1][j]==playerSymb) or (j-1>-1 and gridsym[i][j-1]==playerSymb) or (j+1<5 and gridsym[i][j+1]==playerSymb)): 
        gridresult[i][j]=playerSymb
        if(i-1>-1 and gridsym[i-1][j]!=playerSymb and gridsym[i-1][j]!='*'):
            gridresult[i-1][j]=playerSymb
        if(i+1<5 and gridsym[i+1][j]!=playerSymb and gridsym[i+1][j]!='*'):
            gridresult[i+1][j]=playerSymb
        if(j-1>-1 and gridsym[i][j-1]!=playerSymb and gridsym[i][j-1]!='*'):
            gridresult[i][j-1]=playerSymb
        if(j+1<5 and gridsym[i][j+1]!=playerSymb and gridsym[i][j+1]!='*'):
            gridresult[i][j+1]=playerSymb
    else:
        gridresult[i][j]=playerSymb
    return gridresult
        
f = open(sys.argv[len(sys.argv)-1],"r")

inputlines=f.read().splitlines();
task=inputlines[0]
if int(task)==4:
    debug=0
    playerSym=inputlines[1]
    playerAlgo=inputlines[2]
    playerCutOffDepth=inputlines[3]
    oppPlayerSym=inputlines[4]
    oppPlayerAlgo=inputlines[5]
    oppPlayerCutOffDepth=inputlines[6]
    gridval = [[0 for y in range(5)] for x in range(5)]

    for i in range(0,5):
        for j in range(0,5):
            gridval[i][j]=inputlines[i+7].split()[j] 
    
    gridsym = [[0 for x in range(5)] for x in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            gridsym[i][j]=inputlines[i+12][j]
    rval=[1,2,3,4,5]
    cval=['A','B','C','D','E']
    gridresult = [[0 for y in range(5)]for x in range(5)]
    gridresult=copy.deepcopy(gridsym)
    grid1 = [[0 for y in range(5)]for x in range(5)]
    
    fo = open("trace_state.txt","w")
    fslots=0
    for i in range(0,5):
        for j in range(0,5):
            if(gridresult[i][j]=='*'):
                fslots=fslots+1
    
    while(fslots>0 ):
        
        if int(playerAlgo)==1:
            grid1=GreedyBestFirst(gridresult,gridsym,playerSym)
        elif int(playerAlgo)==2:
            grid1=MiniMaxDecision(gridresult,gridsym,playerSym,playerCutOffDepth)
        elif int(playerAlgo)==3:
            grid1=AlphaBetaSearch(gridresult,gridsym,playerSym,playerCutOffDepth)
        for i in range(0,5):
            for j in range(0,5):
                fo.write( grid1[i][j]);
            if fslots-1>0 or i<4:
                fo.write('\n')
        gridsym=copy.deepcopy(grid1)
        gridresult=copy.deepcopy(grid1)        
        fslots=fslots-1;
        if fslots<1:
            break
        if int(oppPlayerAlgo)==1:
            grid1=GreedyBestFirst(gridresult,gridsym,oppPlayerSym)
        elif int(oppPlayerAlgo)==2:
            grid1=MiniMaxDecision(gridresult,gridsym,oppPlayerSym,oppPlayerCutOffDepth)
        elif int(oppPlayerAlgo)==3:
            grid1=AlphaBetaSearch(gridresult,gridsym,oppPlayerSym,oppPlayerCutOffDepth)
        
        for i in range(0,5):
            for j in range(0,5):
                fo.write( grid1[i][j]);
            if fslots-1>0 or i<4:
                fo.write('\n')
        gridsym=copy.deepcopy(grid1)
        gridresult=copy.deepcopy(grid1)
        fslots=fslots-1;            
    fo.close()
else:    
    debug=1
    playerSym=inputlines[1]
    cutOffDepth=inputlines[2]
    gridval = [[0 for y in range(5)] for x in range(5)]
    
    for i in range(0,5):
        for j in range(0,5):
            gridval[i][j]=inputlines[i+3].split()[j] 
            
    gridsym = [[0 for x in range(5)] for x in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            gridsym[i][j]=inputlines[i+8][j]
    rval=[1,2,3,4,5]
    cval=['A','B','C','D','E']
    gridresult = [[0 for y in range(5)]for x in range(5)]
    gridresult=copy.deepcopy(gridsym)
    if int(task)==1:
        gridresult=GreedyBestFirst(gridresult,gridsym,playerSym)
        
    elif int(task)==2:
        flog2=open("traverse_log.txt", "w")
        flog2.write("Node,Depth,Value")
        gridresult=MiniMaxDecision(gridresult,gridsym,playerSym,cutOffDepth)
        flog2.close()                 
    
    elif int(task)==3:
        flog2=open("traverse_log.txt", "w")
        flog2.write("Node,Depth,Value,Alpha,Beta")
        gridresult=AlphaBetaSearch(gridresult,gridsym,playerSym,cutOffDepth)
        flog2.close()                 
               
    '''
    if task==1:
        
    else:
        print "Wrong Task Value"    
    
        '''
       
    fo = open("next_state.txt", "w")
    for i in range(0,5):
        for j in range(0,5):
            fo.write( gridresult[i][j]);
        if(i<4):
            fo.write('\n')    
    fo.close()
    
# Close opened file
f.close()