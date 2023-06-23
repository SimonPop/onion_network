from onion_network import onion_graph_from_degree_sequence

def test_onion_graph_respects_degree():
    degree_sequence = sorted(
        [
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            4,
            6,
            10
        ]
    )
    G = onion_graph_from_degree_sequence(degree_sequence, seed=1)
    G_degree = sorted([x for _, x in G.degree()])
    assert all([d1 == d2 for d1, d2 in zip(degree_sequence, G_degree)])
