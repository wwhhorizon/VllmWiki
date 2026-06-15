# vllm-project/vllm#13013: [Usage]: audio_language.py - CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#13013](https://github.com/vllm-project/vllm/issues/13013) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: audio_language.py - CUDA out of memory

### Issue 正文摘录

### Your current environment Hello everyone, I wanted to run [audio_language.py](https://github.com/vllm-project/vllm/blob/243137143c81f738db17cfcd93d991f6dd842e27/examples/offline_inference/audio_language.py) with ultravox. To install vllm, I followed the [description of lambda labs](https://docs.lambdalabs.com/public-cloud/on-demand/serving-llama-31-vllm-gh200/): ``` python -m venv vllm-env source vllm-env/bin/activate python -m pip install -U pip setuptools wheel python -m pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124 pip install fsspec[http]==2024.9.0 git clone https://github.com/triton-lang/triton.git cd triton/python && pip install ninja cmake pip install -e . && cd ../../ && rm -rf triton cd $HOME && git clone https://github.com/vllm-project/vllm.git cd vllm && git checkout v0.7.2 && python use_existing_torch.py pip install -r requirements-build.txt && pip install -e . --no-build-isolation ``` Then I run: `vllm serve fixie-ai/ultravox-v0_3 --max-model-len 4096 --trust-remote-code` It works perfectly: ``` INFO 02-10 06:29:54 __init__.py:190] Automatically detected platform cuda. INFO 02-10 06:29:55 api_serve...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: d842e27/examples/offline_inference/audio_language.py) with ultravox. To install vllm, I followed the [description of lambda labs](https://docs.lambdalabs.com/public-cloud/on-demand/serving-llama-31-vllm-gh200/): ``` pyt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lambda labs](https://docs.lambdalabs.com/public-cloud/on-demand/serving-llama-31-vllm-gh200/): ``` python -m venv vllm-env source vllm-env/bin/activate python -m pip install -U pip setuptools wheel python -m pip install...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: l/cu124 pip install fsspec[http]==2024.9.0 git clone https://github.com/triton-lang/triton.git cd triton/python && pip install ninja cmake pip install -e . && cd ../../ && rm -rf triton cd $HOME && git clone https://git...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13013">#13013</a></li> </ul> <h4>Changes</h4> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </detai… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13013">#13013</a></li> </ul> <h4>Changes</h4> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </detai… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
