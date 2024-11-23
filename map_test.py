

result = (
    list(
        map(
            lambda x: x + 1,
            map(
                lambda x: x + 2,
                map(
                    lambda x: x + 3,
                    [1, 2, 3, 4, 5],
                )
            )
        )
    )
)


print(result)

