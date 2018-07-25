import axios from 'source/lib/axios';

const state = {
    tweets: []
};

const getters = {};

const mutations = {
    addTweet(state, tweet) {
        state.tweets = [tweet, ...state.tweets];
    }
};

const actions = {
    async fetchTweets({commit}) {
        const tweets = await axios.get('/api/tweets/');
        tweets.forEach(tweet => commit('addTweet', tweet));
    },

    async createTweet({commit}, data) {
        const tweet = await axios.post('/api/tweets/', data);
        commit('addTweet', tweet);
    }
};

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
};