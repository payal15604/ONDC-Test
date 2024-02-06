{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMzJfhqNLhWR7/mLwxuEpKa",
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
        "<a href=\"https://colab.research.google.com/github/payal15604/ONDC-Test/blob/main/similarity_scoring.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "4h7w-rSCp7aO"
      },
      "outputs": [],
      "source": [
        "import spacy\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nlp= spacy.load(\"en_core_web_sm\")"
      ],
      "metadata": {
        "id": "3ScKqxFjmcX5"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "nlp"
      ],
      "metadata": {
        "id": "e2YT-p4dmkH7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "g1=nlp(\"how\")"
      ],
      "metadata": {
        "id": "7NVcZ7JGmk_U"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "g2=nlp(\"hoe\")"
      ],
      "metadata": {
        "id": "suG7qBIomtVD"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "g2.similarity(g1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vfV4B4Iwmyc0",
        "outputId": "b8ee26c1-750c-4e7d-d7da-f54365f021b1"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-23-8fb83a0f54ab>:1: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.\n",
            "  g2.similarity(g1)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.14732609912851344"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import spacy\n",
        "\n",
        "def calculate_similarity(text1, text2, model=\"en_core_web_sm\"):\n",
        "    # Load the spaCy model\n",
        "    nlp = spacy.load(model)\n",
        "\n",
        "    # Process the texts\n",
        "    doc1 = nlp(text1)\n",
        "    doc2 = nlp(text2)\n",
        "\n",
        "    # Calculate the similarity\n",
        "    similarity_score = doc1.similarity(doc2)\n",
        "\n",
        "    return similarity_score\n",
        "\n",
        "# Example usage:\n",
        "text1 = \"how\"\n",
        "text2 = \"hoe\"\n",
        "similarity = calculate_similarity(text1, text2)\n",
        "print(\"Similarity between '{}' and '{}': {}\".format(text1, text2, similarity))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KRp3vSkcuKCM",
        "outputId": "eb851f90-f517-46a3-84c6-9439d0a2f6f0"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Similarity between 'how' and 'hoe': 0.14732609912851344\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-24-bc710b8375c5>:12: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.\n",
            "  similarity_score = doc1.similarity(doc2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "JzwhVSwgm-dW"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}