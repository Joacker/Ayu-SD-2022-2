FROM golang:1.16-alpine

WORKDIR /backend

RUN apk add --no-cache git curl 

COPY go.mod ./
COPY go.sum ./

COPY . .

RUN go mod download && go mod verify

RUN curl -fLo install.sh https://raw.githubusercontent.com/cosmtrek/air/master/install.sh \    
&& chmod +x install.sh && sh install.sh && cp ./bin/air /bin/air

EXPOSE 3000
RUN air init
CMD ["air"]