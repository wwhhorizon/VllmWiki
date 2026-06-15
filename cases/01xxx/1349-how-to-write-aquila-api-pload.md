# vllm-project/vllm#1349: how to write Aquila api pload? 

| 字段 | 值 |
| --- | --- |
| Issue | [#1349](https://github.com/vllm-project/vllm/issues/1349) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to write Aquila api pload? 

### Issue 正文摘录

when run ` python -m vllm.entrypoints.api_server --model ./AquilaChat2-7B --swap-space 16 --disable-log-requests --host **** --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 2` how to write api prompt ???The following example turns out to be wrong ``` headers = {"User-Agent": "Test Client"} pload = { "prompt": "介绍下广州", "n": 1, # "use_beam_search": True, "temperature": 0, "max_tokens": 300, "stream": True, # "stop": [" "," "], # "stop": [" ", " ",], # "stop": [' '], # "stop_token_ids": [151643, 151644, 151645], } response = requests.post("http://localhost:10860/generate", headers=headers, json=pload, stream=True) ``` ![image](https://github.com/vllm-project/vllm/assets/40717349/4773d2e6-08e8-4ad8-a624-fddc4d87063b)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ad = { "prompt": "介绍下广州", "n": 1, # "use_beam_search": True, "temperature": 0, "max_tokens": 300, "stream": True, # "stop": [" "," "], # "stop": [" ", " ",], # "stop": [' '], # "stop_token_ids": [151643, 151644,
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e Aquila api pload? when run ` python -m vllm.entrypoints.api_server --model ./AquilaChat2-7B --swap-space 16 --disable-log-requests --host **** --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: points.api_server --model ./AquilaChat2-7B --swap-space 16 --disable-log-requests --host **** --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 2` how to write api prompt ???The following exampl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: he following example turns out to be wrong ``` headers = {"User-Agent": "Test Client"} pload = { "prompt": "介绍下广州", "n": 1, # "use_beam_search": True, "temperature": 0, "max_tokens": 300, "stream": True, # "stop": [" ",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
