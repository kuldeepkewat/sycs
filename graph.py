{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP/pCE9PX+ZnncAklH/jVh3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kuldeepkewat/sycs/blob/main/graph.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ruxizZ4l50ta",
        "outputId": "6c6952d8-3ebe-4d35-9ed9-8f4b4fcd140b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['a', 'd'], 'd': ['e'], 'e': ['e']}\n"
          ]
        }
      ],
      "source": [
        "graph_elements={\n",
        "    \"a\":[\"b\",\"c\"],\n",
        "    \"b\":[\"a\",\"d\"],\n",
        "    \"c\":[\"a\",\"d\"],\n",
        "    \"d\":[\"e\"],\n",
        "    \"e\":[\"e\"]\n",
        "}\n",
        "print(graph_elements)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class graph:\n",
        "  def __init__(self,gdict=None):\n",
        "    if gdict is None:\n",
        "      gdict=[]\n",
        "    self.gdict=gdict\n",
        "\n",
        "  def getVertices(self):\n",
        "    return list(self.gdict.keys())\n",
        "\n",
        "graph_elements={\n",
        "    \"a\":[\"b\",\"c\"],\n",
        "    \"b\":[\"a\",\"d\"],\n",
        "    \"c\":[\"a\",\"d\"],\n",
        "    \"d\":[\"e\"],\n",
        "    \"e\":[\"e\"]\n",
        "}\n",
        "g=graph(graph_elements)\n",
        "print(g.getVertices())\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1R2LO0xT6jT-",
        "outputId": "e1afb8a3-ecea-49c9-9d48-746d5324af9c"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['a', 'b', 'c', 'd', 'e']\n"
          ]
        }
      ]
    }
  ]
}