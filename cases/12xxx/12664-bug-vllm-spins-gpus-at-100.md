# vllm-project/vllm#12664: [Bug]: vllm spins gpus at 100%

| 字段 | 值 |
| --- | --- |
| Issue | [#12664](https://github.com/vllm-project/vllm/issues/12664) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm spins gpus at 100%

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Openning a new bug because I don't have permissions to reopen the previous one, sorry if I'm doing this wrong. Fresh pip install of vllm 7.1 in a new venv on ubuntu 24.04 I'm running: vllm serve /home/bruce/Downloads/models/Qwen2.5-32B-Instruct --tensor-parallel-size 2 --max-model-len 12288 --enforce-eager --port 5000 If I ^C out of vllm and then restart it (first killing any processes still hanging on to gpu vram, there is usually one on gpu 1), first query just spins both gpu's at 100% and never returns. tried prefixing the above with: (including doing this at first vllm launch after reboot) NCCL_P2P_DISABLE=1: vllm serve /home/bruce/Downloads/models/Qwen2.5-32B-Instruct --tensor-parallel-size 2 --max-model-len 12288 --enforce-eager --port 5000 no difference. behavior persists till reboot. Here is full console output: First startup log, the curl, then additional console output, then logs at bottom. (vllm) bruce@bruce-AI-Server:~/vllm$ ./vllm-server.sh INFO 02-02 11:49:53 init.py:183] Automatically detected platform cuda. INFO 02-02 11:49:54 api_server.py:838] vLLM API server version 0.7.1 INF...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: vllm spins gpus at 100% bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Openning a new bug because I don't have permissions to reopen the previous one, sorry if I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ns to reopen the previous one, sorry if I'm doing this wrong. Fresh pip install of vllm 7.1 in a new venv on ubuntu 24.04 I'm running: vllm serve /home/bruce/Downloads/models/Qwen2.5-32B-Instruct --tensor-parallel-size...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: type='auto', kv_cache_dtype='auto', max_model_len=12288, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=2, max_parall...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=12288, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: : vllm spins gpus at 100% bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Openning a new bug because I don't have permissions to reopen the previous one, sorry if I'm do...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
