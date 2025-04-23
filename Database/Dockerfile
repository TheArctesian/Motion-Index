FROM docker.elastic.co/elasticsearch/elasticsearch:7.14.0

# Add custom configurations if needed
COPY elasticsearch.yml /usr/share/elasticsearch/config/

# Install plugins if required
# RUN bin/elasticsearch-plugin install analysis-icu

# Set permissions
USER root
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/config/
USER elasticsearch

EXPOSE 9200 9300