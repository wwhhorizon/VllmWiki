# vllm-project/vllm#431: RuntimeError: Failed to import transformers.models.bloom.modeling_bloom because of the following error (look up to see its traceback): /usr/local/lib/python3.8/dist-packages/transformer_engine_extensions.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail23torchInternalAssertFailEPKcS2_jS2_RKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

| 字段 | 值 |
| --- | --- |
| Issue | [#431](https://github.com/vllm-project/vllm/issues/431) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: Failed to import transformers.models.bloom.modeling_bloom because of the following error (look up to see its traceback): /usr/local/lib/python3.8/dist-packages/transformer_engine_extensions.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail23torchInternalAssertFailEPKcS2_jS2_RKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

### Issue 正文摘录

I install vllm via pip in "nvcr.io/nvidia/pytorch:22.12-py3" docker image. When I run the benchmark_throughput.py as follows: `python benchmark_throughput.py --backend=hf --dataset=../benchmark_test_dataset/ShareGPT_V3_unfiltered_cleaned_split.json --model=../huggingface_models/bloom7b1/ --hf-max-batch-size=8` got the follow error : `huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/transformers/utils/import_utils.py", line 1146, in _get_module return importlib.import_module("." + module_name, self.__name__) File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module return _bootstrap._gcd_import(name[level:], package, level) File " ", line 1014, in _gcd_import File " ", line 991, in _find_and_load File " ", line 975, in _find_and_load_unlocked File " ", line 671, in _load_unlocked File " ", line 848, in exec_module Fil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: RuntimeError: Failed to import transformers.models.bloom.modeling_bloom because of the following error (look up to see its traceback): /usr/local/lib/python3.8/dist-packages/transformer_engine_extensions.cpython-38-x86_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: RuntimeError: Failed to import transformers.models.bloom.modeling_bloom because of the following error (look up to see its traceback): /usr/local/lib/python3.8/dist-packages/transformer_engine_extensions.cpython-38-x86_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: a pip in "nvcr.io/nvidia/pytorch:22.12-py3" docker image. When I run the benchmark_throughput.py as follows: `python benchmark_throughput.py --backend=hf --dataset=../benchmark_test_dataset/ShareGPT_V3_unfiltered_cleane...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/transformers/utils/import_utils.py", line 1146, in _get_modul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment varia...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
