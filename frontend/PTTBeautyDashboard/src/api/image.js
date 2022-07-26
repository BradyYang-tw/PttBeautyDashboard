import axios from 'axios'

export const getAllImage = function(){
    return axios({url: "/getAllImage", method: "get"})
}

export const getImageByID = function(id){
    return axios({url:`/getImageByID/${id}`, method: "get"})
}