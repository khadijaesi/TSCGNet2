import numpy as np
import math

def rotate_mesh (mesh, angles):
  #mesh: Le maillage d'origine sous forme de numpy array
  # angles : Les angles de rotation autour des axes X, Y et Z en radians
  # Retourne le maillage 3D résultant après la rotation
  # Extraire les coordonnées des points du maillage

  coordinates = mesh[:, :, :3] # (1, 16000, 3)
  #print('coordinate' , coordinates.shape)
  # Convertir les coordonnées en une liste de points individuels 
  points= np.reshape(coordinates, (-1, 3)) # (16000, 3)
  #print('point' , points.shape)
  # Effectuer la rotation sur chaque point individuellement
  x_angle, y_angle, z_angle = angles 
  cos_x = math.cos(x_angle) 
  sin_x = math.sin(x_angle) 
  cos_y = math.cos(y_angle) 
  sin_y  = math.sin(y_angle)
  cos_z = math.cos(z_angle)
  sin_z= math.sin(z_angle)

  rotation_matrix_x = np.array([[1, 0, 0],[0, cos_x, -sin_x],[0, sin_x, cos_x]])

  rotation_matrix_y= np.array([[cos_y, 0, sin_y],[0, 1, 0],[-sin_y, 0, cos_y]])

  rotation_matrix_z = np.array([[cos_z,-sin_z, 0],[sin_z, cos_z, 0], [0, 0, 1]])

  rotated_points = np.dot (points, rotation_matrix_x)
  rotated_points = np.dot (rotated_points, rotation_matrix_y) 
  rotated_points = np.dot (rotated_points, rotation_matrix_z)

  # Réorganiser les points dans la forme du maillage d'origine
  rotated_mesh = np.reshape(rotated_points, (2, -1, 3)) # (1, 16000, 3)
  #print('rotated_mesh' ,rotated_mesh.shape)
  #print('mesh' ,mesh[:,:, 3:].shape)
  #Ajouter les autres informations du maillage au résultat
  rotated_mesh = np.concatenate((rotated_mesh, mesh[:,:, 3:]), axis=2) # (1, 16000, 24)
  #print('rotated_mesh ba3d concat' ,rotated_mesh.shape)
  return rotated_mesh