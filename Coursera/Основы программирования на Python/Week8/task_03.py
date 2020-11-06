import itertools

print(
    min(
        itertools.filterfalse(
            lambda x: x % 2 == 0,
            map(
                int,
                input().split()
            )
        )
    )
)
