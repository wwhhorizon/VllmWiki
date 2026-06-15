# vllm-project/vllm#32841: [Bug]: The environment variable `VLLM_USE_MODELSCOPE=1` is ineffective when downloading LoRA models.

| 字段 | 值 |
| --- | --- |
| Issue | [#32841](https://github.com/vllm-project/vllm/issues/32841) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The environment variable `VLLM_USE_MODELSCOPE=1` is ineffective when downloading LoRA models.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The environment variable `VLLM_USE_MODELSCOPE=1` is ineffective when downloading LoRA models. I have set the environment variable `VLLM_USE_MODELSCOPE=true`, but when downloading the vllm-ascend/llama32-3b-text2sql-spider model, it still tries to download from Hugging Face, resulting in a connection failure. ``` vllm serve LLM-Research/Llama-3.2-3B-Instruct --enable-lora --lora-modules sql-lora=vllm-ascend/llama32-3b-text2sql-spider ``` The output is following: ``` (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] Error downloading the HuggingFace model (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] Traceback (most recent call last): (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] File "/home/xjy/anaconda3/envs/llm/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 402, in hf_raise_for_status (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] response.raise_for_status() (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] File "/home/xjy/anaconda3/envs/llm/lib/python3.10/site-packages/requests/models.py", line 1026, in raise_for_status (EngineC...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: The environment variable `VLLM_USE_MODELSCOPE=1` is ineffective when downloading LoRA models. bug ### Your current environment ### 🐛 Describe the bug The environment variable `VLLM_USE_MODELSCOPE=1` is ineffectiv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pid=862129) ERROR 01-22 17:44:05 [utils.py:258] Please make sure you specified the correct `repo_id` and `repo_type`. (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] If you are trying to access a private...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: trypoints/cli/main.py", line 73, in main (APIServer pid=861807) args.dispatch_function(args) (APIServer pid=861807) File "/home/xjy/llm_learning/vllm_repo/vllm/entrypoints/cli/serve.py", line 60, in cmd (APIServer pid=8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Hugging Face, resulting in a connection failure. ``` vllm serve LLM-Research/Llama-3.2-3B-Instruct --enable-lora --lora-modules sql-lora=vllm-ascend/llama32-3b-text2sql-spider ``` The output is following: ``` (EngineCor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: y:258] File "/home/xjy/anaconda3/envs/llm/lib/python3.10/site-packages/requests/models.py", line 1026, in raise_for_status (EngineCore_DP0 pid=862129) ERROR 01-22 17:44:05 [utils.py:258] raise HTTPError(http_error_msg,...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
