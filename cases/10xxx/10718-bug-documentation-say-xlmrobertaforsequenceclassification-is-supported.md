# vllm-project/vllm#10718: [Bug]: documentation say XLMRobertaForSequenceClassification is supported but logs say ['XLMRobertaForSequenceClassification'] are not supported for now

| 字段 | 值 |
| --- | --- |
| Issue | [#10718](https://github.com/vllm-project/vllm/issues/10718) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: documentation say XLMRobertaForSequenceClassification is supported but logs say ['XLMRobertaForSequenceClassification'] are not supported for now

### Issue 正文摘录

### Your current environment I install using docker swarm on dedicated cloud vps on hetzner, I want run a lightweight model "jinaai/jina-embeddings-v3", I assume that the cpu and ram i sufficient in a 16gb ram and 4 dedicated cpu. My docker compose file services: jinna: hostname: jinaai image: vllm/vllm-openai:latest command: --trust_remote_code --model jinaai/jina-reranker-v2-base-multilingual --device="cpu" volumes: jinaai:/root/.cache/huggingface environment: HUGGING_FACE_HUB_TOKEN=${secret} networks: ragflow bridge volumes: jinaai: driver: local networks: ragflow: external: true bridge: name: bridge external: true ### Model Input Dumps _No response_ ### 🐛 Describe the bug Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 368, in run_mp_engine raise e File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine engine = MQLLMEngine.from_engine_args(eng...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: docker swarm on dedicated cloud vps on hetzner, I want run a lightweight model "jinaai/jina-embeddings-v3", I assume that the cpu and ram i sufficient in a 16gb ram and 4 dedicated cpu. My docker compose file services:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: '] are not supported for now bug;unstale ### Your current environment I install using docker swarm on dedicated cloud vps on hetzner, I want run a lightweight model "jinaai/jina-embeddings-v3", I assume that the cpu and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 77, in _init_multimodal_config if ModelRegistry.is_multimodal_model(architectures): ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/registry.py",...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: LM', 'MiniCPM3ForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM', 'OlmoeForCausalLM', 'OPTForCausalLM', 'Ori...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
