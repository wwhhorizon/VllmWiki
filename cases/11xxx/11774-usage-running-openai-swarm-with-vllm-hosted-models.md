# vllm-project/vllm#11774: [Usage]: Running OpenAI Swarm with vLLM-hosted models

| 字段 | 值 |
| --- | --- |
| Issue | [#11774](https://github.com/vllm-project/vllm/issues/11774) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Running OpenAI Swarm with vLLM-hosted models

### Issue 正文摘录

### Your current environment Excerpt from running `collect_env.py ` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) Python version: 3.12.0 (main, Oct 3 2023, 01:27:23) [Clang 17.0.1 ] (64-bit runtime) Python platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.31 vLLM Version: 0.6.4.post1 ``` ### How would you like to use vllm I am using the [Swarm](https://github.com/openai/swarm) framework from OpenAI and want to use `meta-llama/Llama-3.1-8B-Instruct` hosted by vllm. I am running the following command to start the vllm server: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct \ --enable-auto-tool-choice \ --tool-call-parser llama3_json \ --chat-template /home/.../repos/vllm/examples/tool_chat_template_llama3.1_json.jinja \ --max_model_len 36192 ``` To run an agent with Swarm, I first define the agent and then run it: ``` datascience_agent = swarm.Agent( name="Data Science Agent", instructions="", functions=[function_X], tool_choice="auto", ) ``` ``` datascience_agent.model = model client = swarm.Swarm(return_client(provider=provider)) conversation = client.run( agent=datascienc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: current environment Excerpt from running `collect_env.py ` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) Python v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `collect_env.py ` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) Python version: 3.12.0 (main, Oct 3 2023, 01:27:2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Running OpenAI Swarm with vLLM-hosted models usage ### Your current environment Excerpt from running `collect_env.py ` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROC...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ing `collect_env.py ` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) Python version: 3.12.0 (main, Oct 3 2023, 01:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nstruct`. I am using function calling. However, I am often getting a `BadRequestError code: 400`. If this error is not thrown, the function calling is not working and the agent is not using a function. Is vllm compatibl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
