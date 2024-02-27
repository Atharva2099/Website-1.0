import streamlit as st

def main():
    st.title("Placeholder lorem epsum loda lasun")
    st.markdown(
        """
        A public documentation of my autism.
        """
    )

    st.subheader("Social Links")
    st.markdown(
        """
        - [LinkedIn](https://www.linkedin.com/in/atharva-w-b0035b214)
        - [GitHub](https://github.com/Atharva2099)
        - [Twitter](https://x.com/attharave)
        """
    )

    st.header("Projects")

    project_cards = [
        {
            "title": "WikiChat",
            "description": "A LLM Chatbot that Scrapes your favourite Wikipedia Page using BeautifulSoup, and answer questions using Mistral7B",
            "github_link": "https://github.com/Atharva2099/My-Portfolio/tree/main/Mistral%20Langchain",
            
        },
        {
            "title": "Dashboard NSE",
            "description": "DashBoard to keep track of your BSE and NSE Stocks portfolio",
            "github_link": "https://github.com/Atharva2099/My-Portfolio/tree/main/Yfinance%20Dashboard%20Streamlit",
            
        }
    ]

    for card in project_cards:
        st.write(f"### {card['title']}")
        st.write(card['description'])
        st.write(f"GitHub: [{card['title']}]({card['github_link']})")


if __name__ == "__main__":
    main()
