# vllm-project/vllm#11055: [Bug, V1]: Service launch failed with v1 code and custom models

| 字段 | 值 |
| --- | --- |
| Issue | [#11055](https://github.com/vllm-project/vllm/issues/11055) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug, V1]: Service launch failed with v1 code and custom models

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Version：0.6.4.post2.dev237+g2a56e126 I start service for my custom models with the code following（Work fine with V0.5.4 & V0 code）： ```Python from vllm import ModelRegistry import runpy import argparse def parse_args(): parser = argparse.ArgumentParser() parser.add_argument("--model", type=str) args, unknow = parser.parse_known_args() return args def model_registry(model_path): import sys sys.path.append(model_path) from modeling_llava_xx import XXCausalLM ModelRegistry.register_model("XXCausalLM", XXCausalLM) if __name__ == "__main__": args = parse_args() model_registry(args.model) runpy.run_module('vllm.entrypoints.openai.api_server', run_name="__main__") ``` For V1，I got an error, which occur at **starting the engine process**： ```Text Traceback (most recent call last): File " ", line 1, in File "/usr/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main exitcode = _main(fd, parent_sentinel) File "/usr/lib/python3.10/multiprocessing/spawn.py", line 128, in _main self = reduction.pickle.load(from_parent) TypeError: _LazyConfigMapping.__init__() missing 1 required positional argume...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: onment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Version：0.6.4.post2.dev237+g2a56e126 I start service for my custom models with the code following（Work fine with V0.5.4 & V0 code）： ```Python from vllm i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: alization parameter mapping. But I don’t know the deserialization mechanism here. （4）Now I have to add model_registry code in `run_engine_core()` in VLLM for registing custom model in new process，and hack `transformers`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug, V1]: Service launch failed with v1 code and custom models bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Version：0.6.4.post2.dev237+g2a56e126 I start service for my cus...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: main self = reduction.pickle.load(from_parent) TypeError: _LazyConfigMapping.__init__() missing 1 required positional argument: 'mapping' ERROR 12-10 06:48:11 core.py:199] EngineCoreProc failed to start. ERROR 12-10 06:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
