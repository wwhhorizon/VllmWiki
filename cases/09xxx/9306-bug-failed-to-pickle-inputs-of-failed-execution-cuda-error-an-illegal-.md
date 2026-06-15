# vllm-project/vllm#9306: [Bug]: Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#9306](https://github.com/vllm-project/vllm/issues/9306) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### Model Input Dumps INFO 10-12 11:34:09 logger.py:36] Received request chat-44505254559d4a72ad36a008ebbfbbdf: prompt: ' system\n你是一个专业且精确的语言判断和翻译工具，你的任务是判断用户输入的字符串是什么语言，并将它翻译为英语，仅需要输出翻译后的结果，不需要描述你的思路或补充性说明等。保持简洁的描述。\n\n**输入类型**：字符串，可能是任何语言，也可能是几种语言的混合，也有可能为空 \n**输出类型**：用户输入的字符串转化为英文后的结果，并用一对连续的英文的大括号包裹。如果用户输入为空，那么输出空值。不需要加入任何前缀后缀或说明性语句，例如“以下是翻译结果”，“Below you are handling the string: ”等，直接输出用大括号包裹后的结果即可。如果你无法理解用户发送的内容，或者用户发送的内容是无意义的字符串，乱码等，你可以直接返回一个用一对大括号包裹的原始字符串。\n\n---\n\n**示例输入1** \nThe Seitai Shinpo Acupuncture Foundation is a non-profit organization whose mission is to foster the development and training of expert teachers and proficient practitioners so that they may perpetuate the wisdom of Seitai Shinpo.\n\n**示例输出1** \n{{The Seitai Shinpo Acupuncture Foundation is a non-profit organization whose mission is to foster the development and training of expert teachers and proficient practitioners so that they may perpetuate the wisdom of Seitai Shinpo.}}\n\n**示例输入2** \n沙特阿拉伯，Mecca的酒店在线预订。良好的可用性和优惠。便宜和安全，在酒店支付，不收预订费。\n\n**示例输出2** \n{{Online hotel booking in Mecca, Saudi Arabia. Good availability and discounts. Affordable and safe, pay at the hotel,...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #9931 [Bugfix] Fix pickle of input when async output processing is on

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: on is to foster the development and training of expert teachers and proficient practitioners so that they may perpetuate the wisdom of Seitai Shinpo.\n\n**示例输出1** \n{{The Seitai Shinpo Acupuncture Foundation is a non-pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: d/demo/anaconda3/envs/vllm_latest/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/raid/demo/anaconda3/envs/vllm_latest/lib/python3.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### Model Input Dumps INFO 10-12 11:34:09 logger.py:36] Received request ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ry access was encountered bug;stale ### Your current environment ### Model Input Dumps INFO 10-12 11:34:09 logger.py:36] Received request chat-44505254559d4a72ad36a008ebbfbbdf: prompt: ' system\n你是一个专业且精确的语言判断和翻译工具，你的任务...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: organization whose mission is to foster the development and training of expert teachers and proficient practitioners so that they may perpetuate the wisdom of Seitai Shinpo.\n\n**示例输出1** \n{{The Seitai Shinpo Acupunctur...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | atest/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0xa0 (0x7f7fc5d49600 in /raid/demo/anaconda3/envs/vllm_l… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | atest/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f7fc5d526fc in /raid/demo/anaconda3/envs/vllm_lates… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | atest/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdbbf4 (0x7f8013500bf4 in /raid/demo/anaconda3/envs/vllm_latest/bin/../lib/libstdc++… |
| [#9931](https://github.com/vllm-project/vllm/pull/9931) | closes_keyword | 0.95 | [Bugfix] Fix pickle of input when async output processing is on | Fix pickle of input when async output processing is on From the log of these issues: #9096 and #9306 ```log WARNING 10-05 21:26:25 model_runner_base.py:143] Failed to pickle in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
