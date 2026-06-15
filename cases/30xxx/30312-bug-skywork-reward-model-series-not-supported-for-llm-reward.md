# vllm-project/vllm#30312: [Bug]: Skywork Reward Model series not supported for `llm.reward`

| 字段 | 值 |
| --- | --- |
| Issue | [#30312](https://github.com/vllm-project/vllm/issues/30312) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Skywork Reward Model series not supported for `llm.reward`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Following https://github.com/vllm-project/vllm/blob/58d5b3f51455706bf4f1f2360a0feb83d161147e/examples/offline_inference/basic/reward.py#L1-L53, I tested `Skywork/Skywork-Reward-V2-Qwen3-0.6B` and the series of Skywork Reward Model, but they didn't work with the `vllm==0.11.2`. I got the following error: ``` INFO 12-09 14:32:57 [llm.py:352] Supported tasks: ['score', 'classify'] Traceback (most recent call last): File "/mnt/ali-sh-1/dataset/zeus/ylqiu/codes/pgen-baselines/amazon/skywork/demo.py", line 53, in main(args) File "/mnt/ali-sh-1/dataset/zeus/ylqiu/codes/pgen-baselines/amazon/skywork/demo.py", line 38, in main outputs = llm.reward(prompts) ^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/non/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 1239, in reward return self.encode( ^^^^^^^^^^^^ File "/root/miniconda3/envs/non/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 1073, in encode raise ValueError(f"pooling_task must be one of {self.supported_tasks}.") ValueError: pooling_task must be one of ['score', 'classify']. ``` It seems the series of the Skywork Reward Model wasn't supported yet. Even tried w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Skywork Reward Model series not supported for `llm.reward` bug ### Your current environment ### 🐛 Describe the bug Following https://github.com/vllm-project/vllm/blob/58d5b3f51455706bf4f1f2360a0feb83d161147e/exam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;nan_inf env_dependency Your current environm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
