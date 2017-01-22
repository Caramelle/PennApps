Rails.application.routes.draw do
  get 'gif/new'
  get 'static/home'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'static#home'
  resources :gifs
end
