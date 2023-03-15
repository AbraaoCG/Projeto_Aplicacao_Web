
    ! Programa Gradiente Descendente (1d linear)
    program GD1d

        integer :: i, j, ie, window, pointsPerWin,ipoint, endPoint, np, numOutInterval,numRetasErro, itmp ,itmp2
        integer :: numVar, npPredDomain
        integer, parameter :: nepochs=10000,  numWin = 1 !
        
        
        real*8 :: erro2, newDomainPCent
        real*8, allocatable :: x(:),y(:),yp(:), dados(:,:),normalizeMask(:)
        real*8, allocatable :: X_NewDomain(:,:), yp_NewDomain(:,:)
        real*8 :: A(numWin), B(numWin), DA(numWin), DB(numWin)
        real*8, parameter:: TA=0.01
        character*100 :: datapath, clixo

        
        open ( unit =  2, file = 'FT_NN_data/output_erro.csv')
        open ( unit =  3, file = 'FT_NN_data/dataPath_Len.txt') ; read(3,'(A100)')datapath    
        open ( unit =  4, file = 'FT_NN_data/output_Pred1.csv')
        open ( unit =  5, file = 'FT_NN_data/output_Pred2.csv')
        open ( unit =  1, file = datapath)
        
        read(3,'(i5)') np
        read(3,'(i5)') numVar
        
        numPredictorsVar = numVar - 1

        newDomainPCent = 0.1
        npPredDomain = int(floor(np * newDomainPCent))
        allocate(x(1:np))
        allocate(y(1:np))
        allocate(yp(1:np))
        allocate(dados(1:np,1:numVar))
        allocate(normalizeMask(1:numVar)) ; normalizeMask(:) = -1e15
        allocate(X_NewDomain(1:npPredDomain,1:numPredictorsVar))
        allocate(yp_NewDomain(1:npPredDomain,1:(numVar-numPredictorsVar) ))
        x(:) = 0.d0 ; y(:) = 0.d0 ; yp(:) = 0.d0 ; dados(:,:) = 0.d0
        pointsPerWin = int(np / numWin)
        numRetasErro = 100
        numOutInterval = int(nepochs / 100)

        read(1,*) clixo


        do i = 1 , np
            
            read(1,*) ( dados(i,j), j = 1,numVar)! , xlixo
            do j = 1,numVar
                if(normalizeMask(j) .lt. dados(i,j)) then
                    normalizeMask(j) = dados(i,j)
                endif
            enddo
        enddo
        
        ! Normalizar dados
        x = dados(:,1) / normalizeMask(1)
        y = dados(:,(numVar)) / normalizeMask(numVar)

        CALL insertionSort(np,dados) ! ordenação dos dados para ser possível segmentar em janelas sequenciais.
        
        
    
        !call date_and_time(VALUES=values2) ! Gera 'semente' inteira para número aleatório oriunda do horário do sistema
        do i = 1,numWin
            !A(i) = values2(1) ; B(i) = values2(2)
            call random_number(HARVEST =  A(i)) ! Gera número real aleatório normalizado.
            call random_number(HARVEST =  B(i)) ! Gera número real aleatório normalizado.
            ! print *, 'A = ',A(i), 'B= ', B(i)
        enddo
    
        ! Definição opcional dos coeficientes usados na reta analisada.
        !Af = 2.d0
        !Bf = 1.0
        ipoint = 1
        endPoint = pointsPerWin
    
        do window = 1,numWin
            do i = ipoint, endPoint
                yp(i) = A(window)*x(i) + B(window)
            enddo
            ipoint = pointsPerWin * window + 1
            endPoint = pointsPerWin * (window + 1)
        enddo
    
        write(2,*)'Epoch,estimateErro' ! 'Epoch,A,B,estimateErro'
    
        erro2 = 1e15
        itmp = 0
        do ie = 1, nepochs
            ipoint = 1
            endPoint = pointsPerWin
    
            DA(:) = 0.d0
            DB(:) = 0.d0
            !erro(ie,:) = 0.d0
            erro2 = 0.d0
    
            do window = 1,numWin
    
               do i = ipoint, endPoint
                   DA(window) = DA(window) + x(i)*( y(i) - yp(i) )
                   DB(window) = DB(window) + 1.0 *( y(i) - yp(i) )
               enddo
    
               DA(window) = -2.0*DA(window)/np
               DB(window) = -2.0*DB(window)/np
    
               A(window) = A(window) - ta*DA(window)
               B(window) = B(window) - ta*DB(window)
    
               do i = ipoint, endPoint
                   yp(i) = A(window)*x(i) + B(window)
               enddo
               ipoint = pointsPerWin * window
               endPoint = pointsPerWin * (window + 1)
            enddo
            do i = 1, np
                erro2 = erro2 +  (y(i) - yp(i))**2
                erro2 = erro2/np
            enddo
            ! Output restrito a um número de linhas para economizar recursos na escrita e leitura desse arquivo,
            ! além da visualização no website
            if (  MOD(itmp,numOutInterval ) .eq. 0) write(2,'(i8,A1,e12.3)')ie,',',erro2 !write(2,'(i8,A1,e12.3,A1,e12.3,A1,e12.3)')ie,',', A(1),',',B(1),',', erro2

            itmp = itmp + 1
        enddo
        
        ! Predição de mais ? = 10 % do dominio inicial para predição futura
        ! Criação randômica do domínio
        rtmp = 0
        do i = 1, npPredDomain
            do j = 1,numPredictorsVar
                call random_number(HARVEST =  rtmp) 
                X_NewDomain(i,j) = ( rtmp * newDomainPCent + 1) ! * normalizeMask(j)
            enddo 
        enddo
        ! Calculo de yPred para novo dominio ( A principio ax+b, mas se tornará mais complexo.)
        itmp = CEILING( (REAL(npPredDomain) / REAL(pointsPerWin) ) ) ! Número de janelas mínimo para representar novos dados a serem preditos.
        ipoint = 1
        endPoint = pointsPerWin
        do window = 1, window
            itmp2 = MOD(window,numWin) + 1
            do i = ipoint, endPoint
                if (i .le. npPredDomain) then
                    yp_NewDomain(i,(numVar-numPredictorsVar)) = ( A(itmp2)*X_NewDomain(i,1) + B(itmp2) ) * normalizeMask(numVar)
                else
                    EXIT
                endif
            enddo
            ipoint = pointsPerWin * window
            endPoint = pointsPerWin * (window + 1)
        enddo
        
        ! Escrita de todo o domínio ( Apenas uma variável pre)
        write(4,'(A6)') 'X,Y'
        write(5,'(A6)') 'X,Y'
        do i = 1, np+npPredDomain
            if(i .le. np) then
                write(4,'(f9.4,A1,f9.4)') x(i) * normalizeMask(1), ',', yp(i)* normalizeMask(numVar)
            else
                write(5,'(f9.4,A1,f9.4)') X_NewDomain(i-np,1) * normalizeMask(1), ',', yp_NewDomain(i-np,(numVar-numPredictorsVar))
            endif

        enddo
        end program
    
    SUBROUTINE insertionSort(numPontosTreino,MatrixDistGrupo)
        integer :: flagSorted, i !, j
        !real*8 :: tmp1,tmp2
        real*8 :: atmp(2)
        integer, INTENT(IN) :: numPontosTreino
        real*8, INTENT(INOUT) :: MatrixDistGrupo(1:numPontosTreino,1:2)
    
    
        flagSorted = -1
        do while ( flagSorted .ne. 1 ) ! Enquanto houver mudança de ordenação na iteração anterior.
            flagSorted = 1
            do i = 1,numPontosTreino - 1 ! iterar sobre todos os pontos comparando 2 a dois e possivelmente trocando as 2 posições
                if (MatrixDistGrupo(i,1) > MatrixDistGrupo(i+1,1) ) then
                    ! se dist(i) > dist(i+1), troco as duas posições, tanto a distância quanto o agrupamento.
                    atmp(:) = MatrixDistGrupo(i+1,:)
                    MatrixDistGrupo(i+1,:) = MatrixDistGrupo(i,:)
                    MatrixDistGrupo(i,:) = atmp(:)
                    !FlagSorted se torna falso.
                    flagSorted = 0
                endif
            enddo
        enddo
    
    END SUBROUTINE
    