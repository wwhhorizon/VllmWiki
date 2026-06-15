# vllm-project/vllm#33596: [CI Failure]:  mi325_1: Multi-Modal Accuracy Eval (Small Models)

| 字段 | 值 |
| --- | --- |
| Issue | [#33596](https://github.com/vllm-project/vllm/issues/33596) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Multi-Modal Accuracy Eval (Small Models)

### Issue 正文摘录

### Name of failing test `pytest -s -v test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename0]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There has been a recent regression in this test group: ```log =================================== FAILURES =================================== _______________ test_lm_eval_correctness_param[config_filename0] _______________ config_filename = PosixPath('/vllm-workspace/.buildkite/lm-eval-harness/configs/Qwen2.5-VL-7B-Instruct.yaml') tp_size = '1' def test_lm_eval_correctness_param(config_filename, tp_size): eval_config = yaml.safe_load(config_filename.read_text(encoding="utf-8")) > results = launch_lm_eval(eval_config, tp_size) test_lm_eval_correctness.py:91: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ test_lm_eval_correctness.py:68: in launch_lm_eval results = lm_eval.simple_evaluate( /usr/local/lib/python3.12/dist-packages/lm_eval/utils.py:498: in _wrapper return fn(*args, **kwargs) /usr/local/lib/python3.12/dist-packages/lm_eval/evaluator.py:366: in simple_evaluate re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [CI Failure]: mi325_1: Multi-Modal Accuracy Eval (Small Models) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename0]` ### Basic information - [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [CI Failure]: mi325_1: Multi-Modal Accuracy Eval (Small Models) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename0]` ### Basic information - [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Multi-Modal Accuracy Eval (Small Models) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename0]` ### Basic information -
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: mi325_1: Multi-Modal Accuracy Eval (Small Models) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename0]` ### Basic information - [...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: True, max_tokens = 512, stop = [' '] kwargs = ({'skip_special_tokens': False, 'spaces_between_special_tokens': False, 'temperature': 0.0}, [], 256) def _multimodal_model_generate( self, requests: List[List[dict]] = None...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
