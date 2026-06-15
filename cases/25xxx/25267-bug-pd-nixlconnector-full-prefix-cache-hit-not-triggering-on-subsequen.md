# vllm-project/vllm#25267: [Bug]: [PD][NixlConnector] Full-prefix cache hit not triggering on subsequent calls

| 字段 | 值 |
| --- | --- |
| Issue | [#25267](https://github.com/vllm-project/vllm/issues/25267) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [PD][NixlConnector] Full-prefix cache hit not triggering on subsequent calls

### Issue 正文摘录

### Your current environment I'm on main `838d7116b` ``` (llmd) ➜ vllm git:(838d7116b) ✗ uv pip show nixl vllm Using Python 3.12.11 environment at: /home/NickLucche/llmd/.venv Name: nixl Version: 0.6.0 Location: /home/NickLucche/llmd/.venv/lib/python3.12/site-packages Requires: numpy, torch Required-by: --- Name: vllm Version: 0.10.2rc3.dev259+g838d7116b.precompiled Location: /home/NickLucche/llmd/.venv/lib/python3.12/site-packages Editable project location: /home/NickLucche/llmd/vllm Requires: aiohttp, blake3, cachetools, cbor2, cloudpickle, compressed-tensors, depyf, diskcache, einops, fastapi, filelock, gguf, lark, llguidance, lm-format-enforcer, mistral-common, msgspec, ninja, numba, numpy, openai, openai-harmony, opencv-python-headless, outlines-core, partial-json-parser, pillow, prometheus-client, prometheus-fastapi-instrumentator, protobuf, psutil, py-cpuinfo, pybase64, pydantic, python-json-logger, pyyaml, pyzmq, ray, regex, requests, scipy, sentencepiece, setproctitle, setuptools, six, tiktoken, tokenizers, torch, torchaudio, torchvision, tqdm, transformers, typing-extensions, watchfiles, xformers, xgrammar Required-by: ``` ### 🐛 Describe the bug I am spinning up a very b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ng Python 3.12.11 environment at: /home/NickLucche/llmd/.venv Name: nixl Version: 0.6.0 Location: /home/NickLucche/llmd/.venv/lib/python3.12/site-packages Requires: numpy, torch Required-by: --- Name: vllm Version: 0.10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: depyf, diskcache, einops, fastapi, filelock, gguf, lark, llguidance, lm-format-enforcer, mistral-common, msgspec, ninja, numba, numpy, openai, openai-harmony, opencv-python-headless, outlines-core, partial-json-parser,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: info, pybase64, pydantic, python-json-logger, pyyaml, pyzmq, ray, regex, requests, scipy, sentencepiece, setproctitle, setuptools, six, tiktoken, tokenizers, torch, torchaudio, torchvision, tqdm, transformers, typing-ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: E_CHANNEL_PORT=47769 UCX_LOG_LEVEL=info VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=6 VLLM_LOGGING_LEVEL="INFO" \ vllm serve Qwen/Qwen3-0.6B --port 48448 --enforce-eager --disable-log-requests --tensor-paralle...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ra stuff ``` # Full prefix cache hit: do not need to read remote blocks, # just notify P worker that we have the blocks we need. num_local_blocks = len(local_block_ids) print("NUM LOCAL BLOCKS", num_local_blocks, "\n",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
