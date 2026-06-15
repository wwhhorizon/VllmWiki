# vllm-project/vllm#13047: [Bug]: `undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE` when running `0.7.3.dev57+g2ae88905.precompiled` on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#13047](https://github.com/vllm-project/vllm/issues/13047) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE` when running `0.7.3.dev57+g2ae88905.precompiled` on A100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This a follow up on #12847. sing the main branch on commit `2ae889052c6d0205ca677052ddb41db96a2a2620`, we are facing `ImportError: /usr/local/lib/python3.12/dist-packages/flash_attn_2_cuda.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE`. The details of the env/test is given below. Adding @youkaichao since I am suspicious #12963 may cause this(?). > [!NOTE] > This issue does NOT happen using 0.7.1 release. On the same machine, same container, changing the installation to `pip install vllm` (or `pip install https://github.com/vllm-project/vllm/releases/download/v0.7.1/vllm-0.7.1-cp38-abi3-manylinux1_x86_64.whl`) works fine. Container/Setup - Container: `nvcr.io/nvidia/pytorch:24.12-py3` - Setup: ``` git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 pip install --editable . ``` Test ```bash python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model meta-llama/Llama-3.2-3B-Instruct --seed 42 -tp 1 --use-v2-block-manager --max_model_len 2048 ``` ```bash INFO 02-10 17:06:23 __init__.py:190] A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: `undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE` when running `0.7.3.dev57+g2ae88905.precompiled` on A100 bug;stale ### Your current environment ### 🐛 D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: IcESaIcEEE` when running `0.7.3.dev57+g2ae88905.precompiled` on A100 bug;stale ### Your current environment ### 🐛 Describe the bug This a follow up on #12847. sing the main branch on commit `2ae889052c6d0205ca677052ddb4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: t 8000 --model meta-llama/Llama-3.2-3B-Instruct --seed 42 -tp 1 --use-v2-block-manager --max_model_len 2048 ``` ```bash INFO 02-10 17:06:23 __init__.py:190] Automatically detected platform cuda. INFO 02-10 17:06:24 api_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ython -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model meta-llama/Llama-3.2-3B-Instruct --seed 42 -tp 1 --use-v2-block-manager --max_model_len 2048 ``` ```bash INFO 02-10 17:06:23 __init__.py:190...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
