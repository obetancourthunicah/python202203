import argparse

def run_args():
  parser = argparse.ArgumentParser(description="Escribe o Muestra Datos de Weather")
  parser.add_argument('--action')
  return parser.parse_args()
