use ndarray::Array2;
use ndarray_csv::Array2Reader;
use std::{error::Error, vec};

fn read_csv() -> Result<Array2<u8>, Box<dyn Error>> {
    let mut reader = csv::ReaderBuilder::new()
        .has_headers(false)
        .from_path("big_graph.csv")?;

    let adj_matrix: Array2<u8> = reader.deserialize_array2((1000, 1000))?;

    Ok(adj_matrix)
}

fn main() {
    // read csv into a two-dimensional Array
    let adj_matrix: Array2<u8> = read_csv().expect("type");

    // determine the source components of the graph with dfs

    let mut visited = vec![false; 1000];

    let mut finish_time: Vec<usize>;

    fn dfs_finish_time(
        u: usize,
        visited: &mut Vec<bool>,
        adj_matrix: &mut Array2<u8>,
        finish_time: &mut Vec<usize>,
    ) {
        visited[u] = true;

        for i in 0..1000 {
            if !visited[i] && adj_matrix[[u, i]] == 1 {
                dfs_finish_time(i, visited, adj_matrix, finish_time);
            }
        }

        finish_time.push(u);
    }

    for vertex in 0..1000 {
        if !visited[vertex] {
            dfs_finish_time(vertex, &mut visited, &mut adj_matrix, &mut finish_time);
        }
    }

    // invert matrix and find components

    let t_adj_matrix = adj_matrix.t().into_owned();

    let mut visited = vec![false; 1000];

    let mut components: Vec<Vec<usize>>;
    let mut num_components: usize = 0;

    fn dfs_tree(
        u: usize,
        visited: &mut Vec<bool>,
        t_adj: &Array2<u8>,
        components: &mut Vec<Vec<usize>>,
        num_components: usize,
    ) {
        visited[u] = true;
        components[num_components].push(u);

        for i in 0..1000 {
            if !visited[i] && t_adj[[u, i]] == 1 {
                dfs_tree(i, visited, t_adj, components, num_components);
            }
        }
    }

    while !finish_time.is_empty() {
        let mut curr_vertex = finish_time.pop().expect("msg");

        if !visited[curr_vertex] {
            dfs_tree(
                curr_vertex,
                &mut visited,
                &t_adj_matrix,
                &mut components,
                num_components,
            );
            num_components += 1;
        }
    }
}
