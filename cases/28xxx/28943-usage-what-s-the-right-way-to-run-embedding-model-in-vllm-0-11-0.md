# vllm-project/vllm#28943: [Usage]: what's the right way to run embedding model in vllm 0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#28943](https://github.com/vllm-project/vllm/issues/28943) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: what's the right way to run embedding model in vllm 0.11.0

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` in vllm 0.8.7，I use following code to run local vllm，all is right： ``` self.engine_args = EngineArgs( model=self.model_path, dtype='half', task="embed", trust_remote_code=True, limit_mm_per_prompt={"image": 1}, ) e = asdict(self.engine_args) self.max_len = 100 self.llm = LLM(**e) out = self.llm.embed(datas) ``` But in vllm 0.11.0 according to the document https://www.aidoczh.com/vllm/models/pooling_models.html，it use runner=='pooling' to run embedding task. What's the diffenence? Could the 'task' arg 'embed' still take effect? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: engine_args = EngineArgs( model=self.model_path, dtype='half', task="embed", trust_remote_code=True, limit_mm_per_prompt={"image": 1}, ) e = asdict(self.engine_args) self.max_len = 100 self.llm = LLM(*
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: what's the right way to run embedding model in vllm 0.11.0 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` in vllm 0.8.7，I use following code to run local vllm，all is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Usage]: what's the right way to run embedding model in vllm 0.11.0 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` in vllm 0.8.7，I use following code to run local vllm，all is r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
