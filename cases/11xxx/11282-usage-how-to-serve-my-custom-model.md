# vllm-project/vllm#11282: [Usage]: How to serve my custom model?

| 字段 | 值 |
| --- | --- |
| Issue | [#11282](https://github.com/vllm-project/vllm/issues/11282) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to serve my custom model?

### Issue 正文摘录

### How would you like to use vllm I have a custom model, and here is my serve code: ``` from vllm import ModelRegistry from transformers import AutoConfig from qwen2_rvs_fast import Qwen2TransConfig, Qwen2TransForCausalLM AutoConfig.register("qwen2trans", Qwen2TransConfig) ModelRegistry.register_model("Qwen2TransForCausalLM", Qwen2TransForCausalLM) import runpy runpy.run_module('vllm.entrypoints.openai.api_server', run_name='__main__') ``` When I run `python my_serve.py --model my_model_path` I got this: INFO 12-18 12:08:19 api_server.py:175] Multiprocessing frontend to use ipc:///tmp/bb074f99-9633-4cf0-a3e2-3043001a3c67 for IPC Path. Traceback (most recent call last): File " ", line 1, in File "/data/zhaocaibei/setup/anaconda3/envs/sf_llm/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main exitcode = _main(fd, parent_sentinel) File "/data/zhaocaibei/setup/anaconda3/envs/sf_llm/lib/python3.10/multiprocessing/spawn.py", line 125, in _main prepare(preparation_data) File "/data/zhaocaibei/setup/anaconda3/envs/sf_llm/lib/python3.10/multiprocessing/spawn.py", line 236, in prepare _fixup_main_from_path(data['init_main_from_path']) File "/data/zhaocaibei/setup/anaconda3/en...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to serve my custom model? usage ### How would you like to use vllm I have a custom model, and here is my serve code: ``` from vllm import ModelRegistry from transformers import AutoConfig from qwen2_rvs_fas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e vllm I have a custom model, and here is my serve code: ``` from vllm import ModelRegistry from transformers import AutoConfig from qwen2_rvs_fast import Qwen2TransConfig, Qwen2TransForCausalLM AutoConfig.register("qwe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
