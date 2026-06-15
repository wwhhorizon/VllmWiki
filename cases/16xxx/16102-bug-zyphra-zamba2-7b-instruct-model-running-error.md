# vllm-project/vllm#16102: [Bug]: Zyphra/Zamba2-7B-Instruct model running error

| 字段 | 值 |
| --- | --- |
| Issue | [#16102](https://github.com/vllm-project/vllm/issues/16102) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Zyphra/Zamba2-7B-Instruct model running error

### Issue 正文摘录

### Your current environment vllm main branch code, run `vllm serve Zyphra/Zamba2-7B-Instruct`. but get error: ``` This flash attention build does not support headdim not being a multiple of 32 ``` look head_size is 224, from https://huggingface.co/Zyphra/Zamba2-7B-Instruct/blob/main/config.json `"attention_head_dim": 224,` this field. this model `Zyphra/Zamba2-1.2B-instruct` is ok, because it head_size is 128. Does anyone know how to fix it? this head_size must be is it an even multiple of an integer? e.g [32,64,128,256] ### 🐛 Describe the bug DEBUG 04-05 10:17:22 [client.py:193] Waiting for output from MQLLMEngine. ERROR 04-05 10:17:25 [engine.py:448] This flash attention build does not support headdim not being a multiple of 32. ERROR 04-05 10:17:25 [engine.py:448] Traceback (most recent call last): ERROR 04-05 10:17:25 [engine.py:448] File "/root/code/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine ERROR 04-05 10:17:25 [engine.py:448] engine = MQLLMEngine.from_vllm_config( ERROR 04-05 10:17:25 [engine.py:448] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-05 10:17:25 [engine.py:448] File "/root/code/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Zyphra/Zamba2-7B-Instruct model running error bug;stale ### Your current environment vllm main branch code, run `vllm serve Zyphra/Zamba2-7B-Instruct`. but get error: ``` This flash attention build does not suppo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ode, run `vllm serve Zyphra/Zamba2-7B-Instruct`. but get error: ``` This flash attention build does not support headdim not being a multiple of 32 ``` look head_size is 224, from https://huggingface.co/Zyphra/Zamba2-7B-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 10:17:25 [engine.py:448] self.model_executor.determine_num_available_blocks()) ERROR 04-05 10:17:25 [engine.py:448] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-05 10:17:25 [engine.py:448] File "/root/c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Zyphra/Zamba2-7B-Instruct model running error bug;stale ### Your current environment vllm main branch code, run `vllm serve Zyphra/Zamba2-7B-Instruct`. but get error: ``` This flash attention build does not suppo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ilable_blocks ERROR 04-05 10:17:25 [engine.py:448] self.model_runner.profile_run() ERROR 04-05 10:17:25 [engine.py:448] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
