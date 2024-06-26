type_defs = """
    type Query {
        ### [Mock] ###
        authenticateUser(request: Request!): Response

        ### [リクエスト機能] ###
        paginatedBookRequests(page: Int!, perPage: Int!, userId: String!, isMyRequest: Boolean!): PaginationData!
        getBookRequest(requestId: ID!): BookRequest

        ### [本検索機能] ###
        searchBooks(page: Int!, perPage: Int!, searchQuery: String): SearchPaginationData!

        ### [ニックネーム取得] ###
        getUserNickname(userId: String!): String

        ### [寄付機能] ###
        getAllBooks: [BookInformation!]

        ### [ユーザー機能] ###
        getUserBookLoans(userId: String!): [BookLoan!]!
    }
"""
