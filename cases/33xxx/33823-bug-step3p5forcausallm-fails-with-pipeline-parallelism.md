# vllm-project/vllm#33823: [Bug]: Step3p5ForCausalLM fails with pipeline parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#33823](https://github.com/vllm-project/vllm/issues/33823) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Step3p5ForCausalLM fails with pipeline parallelism

### Issue 正文摘录

### Your current environment My environment: containers: - name: vllm-leader image: vllm/vllm-openai:nightly-d88a1df699f68e5284fe3a3170f8ae292a3e9c3f env: - name: LWS_GROUP_SIZE valueFrom: fieldRef: fieldPath: metadata.annotations['leaderworkerset.sigs.k8s.io/size'] - name: VLLM_HOST_IP valueFrom: fieldRef: fieldPath: status.podIP - name: HUGGING_FACE_HUB_TOKEN valueFrom: secretKeyRef: name: huggingface-token key: token - name: VLLM_V1_CHECK_LAYER_MAPPING value: "0" - name: VLLM_ATTENTION_BACKEND value: "FLASH_ATTN" - name: VLLM_PP_LAYER_PARTITION value: "13,8,8,8,8" - name: NCCL_IB_DISABLE value: "1" - name: NCCL_P2P_DISABLE value: "1" command: - bash - -c - | set -e export LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH export VLLM_PP_LAYER_PARTITION=13,8,8,8,8 export VLLM_V1_CHECK_LAYER_MAPPING=0 export VLLM_HOST_IP=$(hostname -I | awk '{print $1}') # start Ray head bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=${LWS_GROUP_SIZE} # start vLLM exec python3 -m vllm.entrypoints.openai.api_server \ --model stepfun-ai/Step-3.5-Flash \ --served-model-name MAGIE \ --tensor-parallel-size 1 \ -pp 5 \ --enable-expert-parallel \ --disable-cascade-...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Step3p5ForCausalLM fails with pipeline parallelism bug ### Your current environment My environment: containers: - name: vllm-leader image: vllm/vllm-openai:nightly-d88a1df699f68e5284fe3a3170f8ae292a3e9c3f env: -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: tool-choice \ --tool-call-parser step3p5 \ --quantization fp8 \ --gpu-memory-utilization 0.94 \ --trust-remote-code \ --distributed-executor-backend ray \ --enforce-eager \ --port 8080 ### 🐛 Des
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: valueFrom: fieldRef: fieldPath: metadata.annotations['leaderworkerset.sigs.k8s.io/size'] - name: VLLM_HOST_IP valueFrom: fieldRef: fieldPath: status.podIP - name: HUGGING_FACE_HUB_TOKEN
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: valueFrom: secretKeyRef: name: huggingface-token key: token - name: VLLM_V1_CHECK_LAYER_MAPPING value: "0" - name: VLLM_ATTENTION_BACKEND value: "FLASH_ATTN" - name: VLLM_PP_LAYER_P
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: base.py:344] File "/usr/local/lib/python3.12/dist-packages/ray/util/tracing/tracing_helper.py", line 461, in _resume_span (EngineCore_DP0 pid=563) (RayWorkerWrapper pid=186, ip=10.0.100.135) ERROR 02-04 19:47:43 [worker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
