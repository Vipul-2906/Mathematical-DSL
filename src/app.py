from flask import Flask, request, jsonify, send_from_directory
import time

from lexer import Lexer
from parser import Parser
from solver import Solver

# OPTIONAL (if you want graph images)
try:
    from ast_visualizer import visualize_ast, visualize_parse_tree
    GRAPH_ENABLED = True
except:
    GRAPH_ENABLED = False

app = Flask(__name__, static_folder='static')

# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/compile', methods=['POST'])
def compile_dsl():
    data = request.get_json()
    code = data.get('code', '').strip()

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    start_time = time.time()

    try:
        # ───────────── LEXER ─────────────
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        token_output = "\n".join(str(t) for t in tokens)

        # ───────────── PARSER ─────────────
        parser = Parser(tokens)
        parse_tree, ast = parser.parse()

        trace_output = "\n".join(parser.trace)

        # ───────────── SOLVER ─────────────
        solver = Solver()
        result = solver.solve(ast)

        # ───────────── OPTIONAL GRAPH GENERATION ─────────────
        if GRAPH_ENABLED:
            try:
                visualize_ast(ast)
                visualize_parse_tree(parse_tree)
            except Exception:
                pass  # don’t break UI if graph fails

        # ───────────── TIMING ─────────────
        elapsed = round((time.time() - start_time) * 1000, 2)

        # ───────────── RETURN ─────────────
        return jsonify({
            'tokens': token_output,
            'parse_tree': str(parse_tree),
            'ast': str(ast),
            'trace': trace_output,
            'result': result,
            'time_ms': elapsed,
            'ast_img': '/static/ast_graph.png',
            'parse_img': '/static/parse_tree_graph.png'
        })

    except Exception as e:
        return jsonify({
            'tokens': token_output,
            'parse_tree': str(parse_tree),
            'ast': str(ast),
            'trace': trace_output,
            'result': result,
            'ast_img': '/static/ast_graph.png',
            'parse_img': '/static/parse_tree_graph.png'
        })


# ─────────────────────────────────────────────
# STATIC FILES (for images)
# ─────────────────────────────────────────────

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)


if __name__ == '__main__':
    app.run(debug=True, port=5000)