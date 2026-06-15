# vllm-project/vllm#26881: [Bug]: cli running but debug crashing on flex attention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#26881](https://github.com/vllm-project/vllm/issues/26881) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cli running but debug crashing on flex attention backend

### Issue 正文摘录

The output of python collect_env.py ```text ============================== Versions of relevant libraries ============================== [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.5.1.17 [pip3] nvidia-cufft-cu12==11.3.0.4 [pip3] nvidia-cufile-cu12==1.11.1.6 [pip3] nvidia-curand-cu12==10.3.7.77 [pip3] nvidia-cusolver-cu12==11.7.1.2 [pip3] nvidia-cusparse-cu12==12.5.4.2 [pip3] nvidia-cusparselt-cu12==0.6.3 [pip3] nvidia-ml-py==12.575.51 [pip3] nvidia-nccl-cu12==2.26.2 [pip3] nvidia-nvjitlink-cu12==12.6.85 [pip3] nvidia-nvshmem-cu12==3.3.9 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pynvml==12.0.0 [pip3] pyzmq==27.0.0 [pip3] torch==2.7.1 [pip3] torchaudio==2.7.1+cu128 [pip3] torchvision==0.22.1 [pip3] transformers==4.53.3 [pip3] triton==3.3.1 [conda] Could not collect ``` ### 🐛 Describe the bug I started an online vllm serve using the following launch.json file to test flex attention backend. The benchmark I used is gsm8k bench file from sglang. The problem is, the according cli works well for me but the only problem occurs on the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: utput of python collect_env.py ```text ============================== Versions of relevant libraries ============================== [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ATTENTION python3 -m vllm.entrypoints.api_server --tokenizer-mode auto --model ../models/Meta-Llama-3.1-8B-Instruct/ --disable-log-requests --port 21000 python3 ../sglang/benchmark/gsm8k/bench_other.py --num-questions 2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: cli running but debug crashing on flex attention backend bug;stale The output of python collect_env.py ```text ============================== Versions of relevant libraries ============================== [pip3] n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: == [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.5.1.17 [pip3]...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: l", "cwd": "${workspaceFolder}", "justMyCode": false } ] } ``` ``` ERROR 10-15 12:47:23 [async_llm.py:416] raise self._format_exception(outputs) from None ERROR 10-15 12:47:23 [async_llm.py:416] vllm.v1.engine.exception...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
