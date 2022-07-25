import axios from 'axios'

export const getAllImage = function(){
    return axios({url: "/getAllImage", method: "get"})
}