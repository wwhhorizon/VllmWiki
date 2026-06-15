# vllm-project/vllm#24660: [BUG] [Qwen3-next] MPT+CG fail

| 字段 | 值 |
| --- | --- |
| Issue | [#24660](https://github.com/vllm-project/vllm/issues/24660) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] [Qwen3-next] MPT+CG fail

### Issue 正文摘录

> When I tried MTP with random input from `vllm bench serve` I got the following fail > > ``` > vllm serve $MODEL -tp 4 --served-model-name qwen3-next --tokenizer-mode auto --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' > ``` > > ``` > vllm bench serve --backend vllm --model $MODEL --served-model-name qwen3-next --endpoint /v1/completions --dataset-name random --random-input 2048 --random-output 1024 --max-concurrency 256 --num-prompt 256 > ``` > > ``` > (Worker_TP3 pid=2417047) ERROR 09-11 13:34:02 [multiproc_executor.py:654] File "/home/scratch.vgimpelson_ent/vllm_qwen/vllm/config/__init__.py", line 3380, in pad_for_cudagraph > (Worker_TP3 pid=2417047) ERROR 09-11 13:34:02 [multiproc_executor.py:654] return self.compilation_config.bs_to_padded_graph_size[batch_size] > (Worker_TP3 pid=2417047) ERROR 09-11 13:34:02 [multiproc_executor.py:654] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^ > (Worker_TP3 pid=2417047) ERROR 09-11 13:34:02 [multiproc_executor.py:654] IndexError: list index out of range > ``` The problem somewhere here https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/gdn_attn.py#L211-L215 ``` if (s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [BUG] [Qwen3-next] MPT+CG fail > When I tried MTP with random input from `vllm bench serve` I got the following fail > > ``` > vllm serve $MODEL -tp 4 --served-model-name qwen3-next --tokenizer-mode auto --speculative-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: erve $MODEL -tp 4 --served-model-name qwen3-next --tokenizer-mode auto --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' > ``` > > ``` > vllm bench serve --backend vllm --model $MODEL --se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tp", "num_speculative_tokens": 2}' > ``` > > ``` > vllm bench serve --backend vllm --model $MODEL --served-model-name qwen3-next --endpoint /v1/completions --dataset-name random --random-input 2048 --random-output 1024...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vgimpelson_ent/vllm_qwen/vllm/config/__init__.py", line 3380, in pad_for_cudagraph > (Worker_TP3 pid=2417047) ERROR 09-11 13:34:02 [multiproc_executor.py:654] return self.compilation_config.bs_to_padded_graph_size[batch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
